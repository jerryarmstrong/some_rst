compiler/rustc_const_eval/src/util/mod.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod aggregate;
mod alignment;
mod call_kind;
pub mod collect_writes;
mod compare_types;
mod find_self_call;
mod might_permit_raw_init;
mod type_name;

pub use self::aggregate::expand_aggregate;
pub use self::alignment::is_disaligned;
pub use self::call_kind::{call_kind, CallDesugaringKind, CallKind};
pub use self::compare_types::{is_equal_up_to_subtyping, is_subtype};
pub use self::find_self_call::find_self_call;
pub use self::might_permit_raw_init::might_permit_raw_init;
pub use self::type_name::type_name;


