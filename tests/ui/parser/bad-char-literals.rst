tests/ui/parser/bad-char-literals.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-cr
// ignore-tidy-tab

fn main() {
    // these literals are just silly.
    ''';
    //~^ ERROR: character constant must be escaped: `'`

    // note that this is a literal "\n" byte
    '
';
    //~^^ ERROR: character constant must be escaped: `\n`

    // note that this is a literal "\r" byte
    ''; //~ ERROR: character constant must be escaped: `\r`

    // note that this is a literal tab character here
    '	';
    //~^ ERROR: character constant must be escaped: `\t`
}


