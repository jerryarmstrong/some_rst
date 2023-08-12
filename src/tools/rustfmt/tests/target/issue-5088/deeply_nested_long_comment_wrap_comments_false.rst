src/tools/rustfmt/tests/target/issue-5088/deeply_nested_long_comment_wrap_comments_false.rs
===========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: false

fn main() {
    {
        {
            {
                {
                    {
                        {
                            {
                                {
                                    {
                                        {
                                            {
                                                // - aaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa bbbbbbbbbb bbbbbbbbb bbbbbbbbb ccc cccccccccc ccccccc cccccccc

                                                // * aaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa bbbbbbbbbb bbbbbbbbb bbbbbbbbb ccc cccccccccc ccccccc cccccccc

                                                /* - aaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa bbbbbbbbbb bbbbbbbbb bbbbbbbbb ccc cccccccccc ccccccc cccccccc */

                                                /* * aaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa bbbbbbbbbb bbbbbbbbb bbbbbbbbb ccc cccccccccc ccccccc cccccccc */
                                            };
                                        };
                                    };
                                };
                            };
                        };
                    };
                };
            };
        };
    };
}


