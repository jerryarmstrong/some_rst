tests/ui/regions/regions-return-interior-of-option.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn get<T>(opt: &Option<T>) -> &T {
    match *opt {
      Some(ref v) => v,
      None => panic!("none")
    }
}

pub fn main() {
    let mut x = Some(23);

    {
        let y = get(&x);
        assert_eq!(*y, 23);
    }

    x = Some(24);

    {
        let y = get(&x);
        assert_eq!(*y, 24);
    }
}


