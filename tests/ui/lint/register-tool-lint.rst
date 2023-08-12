tests/ui/lint/register-tool-lint.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(register_tool)]
#![register_tool(xyz)]
#![warn(xyz::my_lint)] // this should not error
#![warn(abc::my_lint)]
//~^ ERROR unknown tool name `abc` found in scoped lint
//~| HELP add `#![register_tool(abc)]`
//~| ERROR unknown tool name `abc`
//~| HELP add `#![register_tool(abc)]`


