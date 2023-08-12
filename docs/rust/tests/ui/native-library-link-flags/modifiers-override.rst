tests/ui/native-library-link-flags/modifiers-override.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-ldylib:+as-needed=foo -lstatic=bar -Zunstable-options

#[link(name = "foo")]
#[link(
    name = "bar",
    kind = "static",
    modifiers = "+whole-archive,-whole-archive",
    //~^ ERROR multiple `whole-archive` modifiers in a single `modifiers` argument
    modifiers = "+bundle"
    //~^ ERROR multiple `modifiers` arguments in a single `#[link]` attribute
)]
extern "C" {}
//~^ ERROR overriding linking modifiers from command line is not supported
//~| ERROR overriding linking modifiers from command line is not supported

fn main() {}


