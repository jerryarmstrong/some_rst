tests/ui/closures/binder/implicit-stuff.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(closure_lifetime_binder)]

fn main() {
    // Implicit types
    let _ = for<> || {};                                      //~ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
    let _ = for<'a> || -> &'a _ { &() };                      //~ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
    let _ = for<'a> |x| -> &'a () { x };                      //~ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
    let _ = for<'a> |x: &'a _| -> &'a () { x };               //~ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
    let _ = for<'a> |x: &'a Vec::<_>| -> &'a Vec::<()> { x }; //~ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
    let _ = for<'a> |x: &'a Vec<()>| -> &'a Vec<_> { x };     //~ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
    let _ = for<'a> |x: &'a _| -> &'a &'a () { x };           //~ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
    let _ = for<'a> |x: &'a _, y, z: _| -> &'a _ {            //~ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
        let _: &u8 = x;
        let _: u32 = y;
        let _: i32 = z;
        x
    };

    // Lifetime elision
    let _ = for<> |_: &()| -> () {};           //~ ERROR `&` without an explicit lifetime name cannot be used here
    let _ = for<> |x: &()| -> &() { x };       //~ ERROR `&` without an explicit lifetime name cannot be used here
                                               //~| ERROR `&` without an explicit lifetime name cannot be used here
    let _ = for<> |x: &'_ ()| -> &'_ () { x }; //~ ERROR `'_` cannot be used here
                                               //~| ERROR `'_` cannot be used here
    let _ = for<'a> |x: &()| -> &'a () { x };  //~ ERROR `&` without an explicit lifetime name cannot be used here
    let _ = for<'a> |x: &'a ()| -> &() { x };  //~ ERROR `&` without an explicit lifetime name cannot be used here
}


