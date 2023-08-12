storage/libradb/src/ledger_counters/test.rs
===========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use super::*;

#[test]
fn test_ledger_counters() {
    // Defaults to 0.
    let mut counters = LedgerCounters::new();
    assert_eq!(counters.get(LedgerCounter::NewStateLeaves), 0);

    // Bump
    let mut bumps = LedgerCounterBumps::new();
    bumps
        .bump(LedgerCounter::NewStateLeaves, 1)
        .bump(LedgerCounter::StaleStateLeaves, 1);
    counters.bump(bumps);
    assert_eq!(counters.get(LedgerCounter::NewStateLeaves), 1);
    assert_eq!(counters.get(LedgerCounter::StaleStateLeaves), 1);

    // Bump again.
    let mut bumps = LedgerCounterBumps::new();
    bumps
        .bump(LedgerCounter::EventsCreated, 1)
        .bump(LedgerCounter::NewStateLeaves, 1);
    counters.bump(bumps);
    assert_eq!(counters.get(LedgerCounter::EventsCreated), 1);
    assert_eq!(counters.get(LedgerCounter::NewStateLeaves), 2);
    assert_eq!(counters.get(LedgerCounter::StaleStateLeaves), 1);
}


