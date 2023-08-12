tests/ui/rfc-2497-if-let-chains/invalid-let-in-a-valid-let-context.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(let_chains)]

fn main() {
    let _opt = Some(1i32);

    #[cfg(FALSE)]
    {
        let _ = &&let Some(x) = Some(42);
        //~^ ERROR expected expression, found `let` statement
    }
    #[cfg(FALSE)]
    {
        if let Some(elem) = _opt && [1, 2, 3][let _ = &&let Some(x) = Some(42)] = 1 {
        //~^ ERROR expected expression, found `let` statement
        //~| ERROR expected expression, found `let` statement
            true
        }
    }

    #[cfg(FALSE)]
    {
        if let Some(elem) = _opt && {
            [1, 2, 3][let _ = ()];
            //~^ ERROR expected expression, found `let` statement
            true
        } {
        }
    }

    #[cfg(FALSE)]
    {
        if let Some(elem) = _opt && [1, 2, 3][let _ = ()] = 1 {
        //~^ ERROR expected expression, found `let` statement
            true
        }
    }
    #[cfg(FALSE)]
    {
        if let a = 1 && {
            let x = let y = 1;
            //~^ ERROR expected expression, found `let` statement
        } {
        }
    }
}


