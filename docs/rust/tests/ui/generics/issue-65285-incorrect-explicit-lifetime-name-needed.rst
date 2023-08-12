tests/ui/generics/issue-65285-incorrect-explicit-lifetime-name-needed.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

struct Nested<K>(K);

fn should_error<T>() where T : Into<&u32> {}
//~^ ERROR `&` without an explicit lifetime name cannot be used here [E0637]

trait X<'a, K: 'a> {
    fn foo<'b, L: X<&'b Nested<K>>>();
    //~^ ERROR missing lifetime specifier [E0106]
    //~| ERROR the type `&'b Nested<K>` does not fulfill the required lifetime
}

fn bar<'b, L: X<&'b Nested<i32>>>(){}
//~^ ERROR missing lifetime specifier [E0106]


