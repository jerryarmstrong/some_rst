src/tools/rustfmt/tests/source/struct_lits_visual_multiline.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true
// rustfmt-wrap_comments: true
// rustfmt-indent_style: Visual
// rustfmt-struct_lit_single_line: false

// Struct literal expressions.

fn main() {
    let x = Bar;

    // Comment
    let y = Foo {a: x };

    Foo { a: foo() /* comment*/, /* comment*/ b: bar(), ..something };

    Fooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo { a: foo(), b: bar(), };

    Foooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo {
        // Comment
        a: foo(), // Comment
        // Comment
        b: bar(), // Comment
    };

    Foo { a:Bar,
          b:foo() };

    Quux { x: if cond { bar(); }, y: baz() };

    A {
    // Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor.
    first: item(),
        // Praesent et diam eget libero egestas mattis sit amet vitae augue.
        // Nam tincidunt congue enim, ut porta lorem lacinia consectetur.
        second: Item
    };

    Diagram { /*                 o        This graph demonstrates how
               *                / \       significant whitespace is
               *               o   o      preserved.
               *              /|\   \
               *             o o o   o */
              graph: G, }
}


