tests/ui/suggestions/suggest_print_over_printf.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Suggest print macro when user erroneously uses printf

fn main() {
    let x = 4;
    printf("%d", x);
    //~^ ERROR cannot find function `printf` in this scope
    //~| HELP you may have meant to use the `print` macro
}


