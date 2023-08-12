src/tools/rustfmt/tests/source/issue-1210/e.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_strings: true
// rustfmt-max_width: 50

// explicit line breaks should be kept in order to preserve the layout

const foo: String = "Suspendisse vel augue at felis tincidunt sollicitudin. Fusce arcu.
               Duis et odio et leo
        sollicitudin consequat. Aliquam lobortis.  Phasellus condimentum.";


