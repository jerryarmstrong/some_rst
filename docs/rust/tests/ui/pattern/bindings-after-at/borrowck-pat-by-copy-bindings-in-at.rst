tests/ui/pattern/bindings-after-at/borrowck-pat-by-copy-bindings-in-at.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Test `Copy` bindings in the rhs of `@` patterns.

#[derive(Copy, Clone)]
struct C;

fn mk_c() -> C { C }

#[derive(Copy, Clone)]
struct P<A, B>(A, B);

enum E<A, B> { L(A), R(B) }

fn main() {
    let a @ b @ c @ d = C;
    let a @ (b, c) = (C, mk_c());
    let a @ P(b, P(c, d)) = P(mk_c(), P(C, C));
    let a @ [b, c] = [C, C];
    let a @ [b, .., c] = [C, mk_c(), C];
    let a @ [b, mid @ .., c] = [C, mk_c(), C];
    let a @ &(b, c) = &(C, C);
    let a @ &(b, &P(c, d)) = &(mk_c(), &P(C, C));

    fn foo(a @ [b, mid @ .., c]: [C; 3]) {}

    use self::E::*;
    match L(C) {
        L(a) | R(a) => {
            let a: C = a;
            drop(a);
            drop(a);
        }
    }
    match R(&L(&mk_c())) {
        L(L(&a)) | L(R(&a)) | R(L(&a)) | R(R(&a)) => {
            let a: C = a;
            drop(a);
            drop(a);
        }
    }

    match Ok(mk_c()) {
        Ok(ref a @ b) | Err(b @ ref a) => {
            let _: &C = a;
            let _: C = b;
        }
    }
}


