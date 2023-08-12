tests/ui/parser/wrong-escape-of-curly-braces.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let ok = "{{everything fine}}";
    let bad = "\{it is wrong\}";
    //~^  ERROR unknown character escape: `{`
    //~|  HELP if used in a formatting string, curly braces are escaped with `{{` and `}}`
    //~| ERROR unknown character escape: `}`
    //~| HELP if used in a formatting string, curly braces are escaped with `{{` and `}}`
}


