tests/ui/lazy-type-alias-impl-trait/infer_cross_function.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

trait Reader {}

struct Unit<R>(R);
struct ResDwarf<R>(R);

struct Context<R: Reader> {
    dwarf: ResDwarf<R>,
}

struct Range;

struct ResUnit<R>(R);

impl<R: Reader + 'static> Context<R> {
    fn find_dwarf_unit(&self, probe: u64) -> Option<&Unit<R>> {
        let x = self.find_units(probe);
        None
    }

    fn find_units(&self, probe: u64) -> impl Iterator<Item = &ResUnit<R>> {
        std::iter::empty()
    }
}


