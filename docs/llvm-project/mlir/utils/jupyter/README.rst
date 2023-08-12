mlir/utils/jupyter/README.md
============================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: md

    A Jupyter kernel for mlir (mlir-opt)

This is purely for experimentation. This kernel uses the reproducer runner
conventions to run passes.

To install:

    python3 -m mlir_opt_kernel.install

To use it, run one of:

```shell
    jupyter notebook
    # In the notebook interface, select MlirOpt from the 'New' menu
    jupyter console --kernel mlir
```

`mlir-opt` is expected to be either in the `PATH` or `MLIR_OPT_EXECUTABLE` is
used to point to the executable directly.


