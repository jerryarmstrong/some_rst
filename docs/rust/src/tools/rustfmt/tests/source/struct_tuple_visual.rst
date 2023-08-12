src/tools/rustfmt/tests/source/struct_tuple_visual.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true
// rustfmt-wrap_comments: true
// rustfmt-indent_style: Visual
fn foo() {
    Fooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(f(), b());

    Foooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(// Comment
                                                                                      foo(), /* Comment */
                                                                                      // Comment
                                                                                      bar() /* Comment */);

    Foo(Bar, f());

    Quux(if cond {
             bar();
         },
         baz());

    Baz(xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,
        zzzzz /* test */);

    A(// Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit
      // amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante
      // hendrerit. Donec et mollis dolor.
      item(),
      // Praesent et diam eget libero egestas mattis sit amet vitae augue.
      // Nam tincidunt congue enim, ut porta lorem lacinia consectetur.
      Item);

    Diagram(//                 o        This graph demonstrates how
            //                / \       significant whitespace is
            //               o   o      preserved.
            //              /|\   \
            //             o o o   o
            G)
}


