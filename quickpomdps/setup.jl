module PyQuickPOMDPs

using PyCall
inspect = pyimport("inspect")

import QuickPOMDPs

function QuickPOMDPs.preprocess(v::PyObject)
    if pybuiltin("callable")(v)
        return convert(Function, v)
    end

    return v
end

function QuickPOMDPs.preprocess(name::Union{Val{:reward},Val{:observation}}, v::PyObject)
    if pybuiltin("callable")(v)
        n_required, n_optional = argcounts(v)
        return vararg_closure(name, Val(n_required), Val(n_optional), v)
    end

    return v
end

# here is where the bass drops. Probably easier to file an issue and tag @zsunberg than try to understand this
macro provide_vararg_closure(basename::Symbol, n_required::Int, n_optional::Union{Int,Float64})
    name = Symbol(String(basename)*"_pyfunc_closure")
    if n_optional < 0
        argnames = [Symbol("arg"*string(i)) for i in 1:n_required]
        methods = [:($name($(argnames...), a...) = v($(argnames...), a...))]
    else
        methods = [:($name(a::Vararg{Any,$(n_required)}) = v(a...))]
        for i in 1:n_optional
            push!(methods, :($name(a::Vararg{Any,$(n_required+i)}) = v(a...)))
        end
    end
    fname = esc(:vararg_closure)
    return quote
        function $fname(::Val{$(Meta.quot(basename))}, ::Val{$n_required}, ::Val{$n_optional}, v)
            $(methods...)
            return $name
        end
    end
end

@provide_vararg_closure(observation, 1, 0)
@provide_vararg_closure(observation, 1, 1)
@provide_vararg_closure(observation, 1, 2)
@provide_vararg_closure(observation, 1, -1)
@provide_vararg_closure(observation, 2, 0)
@provide_vararg_closure(observation, 2, 1)
@provide_vararg_closure(observation, 2, -1)
@provide_vararg_closure(observation, 3, 0)
@provide_vararg_closure(observation, 3, -1)

@provide_vararg_closure(reward, 2, 0)
@provide_vararg_closure(reward, 2, 1)
@provide_vararg_closure(reward, 2, 2)
@provide_vararg_closure(reward, 2, -1)
@provide_vararg_closure(reward, 3, 0)
@provide_vararg_closure(reward, 3, 1)
@provide_vararg_closure(reward, 3, -1)
@provide_vararg_closure(reward, 4, 0)
@provide_vararg_closure(reward, 4, -1)

"""
Assuming there are no keyword arguments, return the number of required and optional arguments (-1 for arbitrarily many optional).
"""
function argcounts(v::PyObject)
    params = inspect.signature(v).parameters.values()
    n_required = count(params) do p
        if p.kind==p.POSITIONAL_ONLY || p.kind==p.POSITIONAL_OR_KEYWORD
            return p.default == p.empty
        else
            return false
        end
    end
    if any(p->p.kind==p.VAR_POSITIONAL, params)
        n_optional = -1
    else
        n_optional = count(params) do p
            if p.kind==p.POSITIONAL_ONLY || p.kind==p.POSITIONAL_OR_KEYWORD
                return p.default != p.empty
            else
                return false
            end
        end
    end
    return n_required, n_optional
end

end #module
