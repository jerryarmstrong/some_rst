tests/ui/parser/issues/issue-1655.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod blade_runner {
    #vec[doc( //~ ERROR expected one of `!` or `[`, found `vec`
        brief = "Blade Runner is probably the best movie ever",
        desc = "I like that in the world of Blade Runner it is always
                raining, and that it's always night time. And Aliens
                was also a really good movie.

                Alien 3 was crap though."
    )]
}


