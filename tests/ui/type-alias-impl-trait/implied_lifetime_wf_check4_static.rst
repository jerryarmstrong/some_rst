tests/ui/type-alias-impl-trait/implied_lifetime_wf_check4_static.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

mod test_type_param_static {
    type Ty<A> = impl Sized + 'static;
    //~^ ERROR: the parameter type `A` may not live long enough
    fn defining<A: 'static>(s: A) -> Ty<A> { s }
    fn assert_static<A: 'static>() {}
    fn test<A>() where Ty<A>: 'static { assert_static::<A>() }
}

fn main() {}


