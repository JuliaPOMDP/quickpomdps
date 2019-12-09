using PyCall

import QuickPOMDPs: preprocess

function preprocess(v::PyObject)
    if pybuiltin("callable")(v)
        return convert(Function, v)
    end

    return v
end

# TODO
# Actually convert the callables
# Maybe we can g
