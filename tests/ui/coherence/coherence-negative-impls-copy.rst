tests/ui/coherence/coherence-negative-impls-copy.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// regression test for issue #101836

#![feature(negative_impls, extern_types)]
#![crate_type = "lib"]

struct NonCopy;
struct NeverCopy(NonCopy);

impl !Copy for NeverCopy {}


struct WithDrop;
impl Drop for WithDrop { fn drop(&mut self) {} }

impl !Copy for WithDrop {}


struct Type;
trait Trait {}
extern {
    type ExternType;
}

impl !Copy for &mut Type {}

impl !Copy for dyn Trait {}

impl !Copy for ExternType {}


