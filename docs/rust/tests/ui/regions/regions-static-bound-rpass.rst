tests/ui/regions/regions-static-bound-rpass.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn invariant_id<'a,'b>(t: &'b mut &'static ()) -> &'b mut &'a ()
    where 'a: 'static { t }
//~^ WARN unnecessary lifetime parameter `'a`

fn static_id<'a>(t: &'a ()) -> &'static ()
    where 'a: 'static { t }
//~^ WARN unnecessary lifetime parameter `'a`

fn static_id_indirect<'a,'b>(t: &'a ()) -> &'static ()
    where 'a: 'b, 'b: 'static { t }
//~^ WARN unnecessary lifetime parameter `'b`

fn ref_id<'a>(t: &'a ()) -> &'a () where 'static: 'a { t }

static UNIT: () = ();

fn main()
{
    let mut val : &'static () = &UNIT;
    invariant_id(&mut val);
    static_id(val);
    static_id_indirect(val);
    ref_id(val);
}


