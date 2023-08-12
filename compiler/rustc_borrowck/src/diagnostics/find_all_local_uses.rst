compiler/rustc_borrowck/src/diagnostics/find_all_local_uses.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustc::untranslatable_diagnostic)]
#![deny(rustc::diagnostic_outside_of_impl)]

use std::collections::BTreeSet;

use rustc_middle::mir::visit::{PlaceContext, Visitor};
use rustc_middle::mir::{Body, Local, Location};

/// Find all uses of (including assignments to) a [`Local`].
///
/// Uses `BTreeSet` so output is deterministic.
pub(super) fn find(body: &Body<'_>, local: Local) -> BTreeSet<Location> {
    let mut visitor = AllLocalUsesVisitor { for_local: local, uses: BTreeSet::default() };
    visitor.visit_body(body);
    visitor.uses
}

struct AllLocalUsesVisitor {
    for_local: Local,
    uses: BTreeSet<Location>,
}

impl<'tcx> Visitor<'tcx> for AllLocalUsesVisitor {
    fn visit_local(&mut self, local: Local, _context: PlaceContext, location: Location) {
        if local == self.for_local {
            self.uses.insert(location);
        }
    }
}


