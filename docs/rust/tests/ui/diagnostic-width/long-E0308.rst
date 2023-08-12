tests/ui/diagnostic-width/long-E0308.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --diagnostic-width=60
// normalize-stderr-test: "long-type-\d+" -> "long-type-hash"

mod a {
    // Force the "short path for unique types" machinery to trip up
    pub struct Atype;
    pub struct Btype;
    pub struct Ctype;
}

mod b {
    pub struct Atype<T, K>(T, K);
    pub struct Btype<T, K>(T, K);
    pub struct Ctype<T, K>(T, K);
}

use b::*;

fn main() {
    let x: Atype<
      Btype<
        Ctype<
          Atype<
            Btype<
              Ctype<
                Atype<
                  Btype<
                    Ctype<i32, i32>,
                    i32
                  >,
                  i32
                >,
                i32
              >,
              i32
            >,
            i32
          >,
          i32
        >,
        i32
      >,
      i32
    > = Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(
        Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(
            Ok("")
        ))))))))))))))))))))))))))))))
    ))))))))))))))))))))))))))))));
    //~^^^^^ ERROR E0308

    let _ = Some(Ok(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(
        Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(
            Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(Some(
                Some(Some(Some(Some(Some(Some(Some(Some(Some("")))))))))
            )))))))))))))))))
        ))))))))))))))))))
    ))))))))))))))))) == Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(
        Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(
            Ok(Ok(Ok(Ok(Ok(Ok(Ok("")))))))
        ))))))))))))))))))))))))))))))
    ))))))))))))))))))))))));
    //~^^^^^ ERROR E0308

    let x: Atype<
      Btype<
        Ctype<
          Atype<
            Btype<
              Ctype<
                Atype<
                  Btype<
                    Ctype<i32, i32>,
                    i32
                  >,
                  i32
                >,
                i32
              >,
              i32
            >,
            i32
          >,
          i32
        >,
        i32
      >,
      i32
    > = ();
    //~^ ERROR E0308

    let _: () = Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(
        Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(Ok(
            Ok(Ok(Ok(Ok(Ok(Ok(Ok("")))))))
        ))))))))))))))))))))))))))))))
    ))))))))))))))))))))))));
    //~^^^^^ ERROR E0308
}


