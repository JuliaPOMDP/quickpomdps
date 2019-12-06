using PyCall

function convert_pyobjects!(kwd::Dict)
    for (k, v) in kwd
        if v isa PyObject && pybuiltin("callable")(v)
            kwd[k] = convert(Function, v)
        end
    end
end

# TODO
# Actually convert the callables
# Maybe we can g
