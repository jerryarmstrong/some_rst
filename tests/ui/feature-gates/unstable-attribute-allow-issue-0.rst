tests/ui/feature-gates/unstable-attribute-allow-issue-0.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that an issue value can be explicitly set to "0" instead of "none"
#![crate_type = "lib"]
#![feature(staged_api)]
#![stable(feature = "stable_test_feature", since = "1.0.0")]

#[unstable(feature = "unstable_test_feature", issue = "0")]
fn unstable_issue_0() {} //~^ ERROR `issue` must be a non-zero numeric string or "none"

#[unstable(feature = "unstable_test_feature", issue = "none")]
fn unstable_issue_none() {}

#[unstable(feature = "unstable_test_feature", issue = "something")]
fn unstable_issue_not_allowed() {} //~^ ERROR `issue` must be a non-zero numeric string or "none"


