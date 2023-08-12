language/tools/move-mv-llvm-compiler/docs/TypeInfo.md
=====================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: md

    # Type info in the binary

Goes in a separate ELF section. For now the compiler emits BTF however this can change in future based on the requirements of the environment.


## Purpose of type info
- For debugging
- For rejecting invalid programs. The type info should not be used to **accept** a program because typeinfo can be manipulated outside of the program.


