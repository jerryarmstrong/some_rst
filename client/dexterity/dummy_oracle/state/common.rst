client/dexterity/dummy_oracle/state/common.py
=============================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    from podite import U8, Enum, pod


@pod
class AccountTag(Enum[U8]):
    UNINITIALIZED = None
    ORACLE_PRICE = None


