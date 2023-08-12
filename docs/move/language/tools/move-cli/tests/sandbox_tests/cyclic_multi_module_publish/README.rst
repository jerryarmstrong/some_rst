language/tools/move-cli/tests/sandbox_tests/cyclic_multi_module_publish/README.md
=================================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: md

    ## Test Case Explanation

The goal of this test case is to check that the VM properly rejects a module
with cyclic dependencies even in the multi-module publishing setting.

Here is the procedure:

1. publish two modules with dependencies `B --depends_on--> A`.

   (See the code in package `p1`)


2. compile a set of modules with dependencies `A --may_use--> C --depends_on--> B'`

   (See the code in package `p2`)

   NOTE that module `B'` is an update to module `B` with dependency to module
   `A` removed.  We need this tweak here, otherwise, the compiler will flag the
   cyclic dependency and we can never reach the publishing step to test the VM.


3. publish the modules compiled in step 2, but only module `A` and `C` with the
   `--override-ordering` flag. Without this flag, all modules will be published.

   This will trigger the check on the VM side and the VM aborts correctly with
   `INVALID_FRIEND_DECL_WITH_MODULES_IN_DEPENDENCIES`.


