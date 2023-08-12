src/report.rs
=============

Last edited: 2021-09-02 06:22:54

Contents:

.. code-block:: rs

    use {
    crate::token::TokenAccountEntry,
    serde::{Deserialize, Serialize},
    solana_sdk::pubkey::Pubkey,
    std::{collections::HashMap, io::Write},
};

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
pub struct Report {
    pub entries_by_token_address: HashMap<Pubkey, TokenAccountEntry>,
}

impl Report {
    pub fn new() -> Self {
        Self {
            entries_by_token_address: HashMap::new(),
        }
    }

    /// Output the report as csv for easy reading
    ///
    /// There are three different types of transactions to report:
    ///   * possibly fraudulent transfers and burns
    ///   * owner assignment
    ///   * approvals
    ///
    /// Transfers and burns will only be reported if they are signed by a key
    /// that is not the current owner, and there was an owner assignment at
    /// some point. These transactions must be investigated further to discover
    /// any loss of funds.
    ///
    /// This way, it's easy to search each of these transactions on the explorer
    /// or other tools to see the chain of malicious transactions as needed.
    pub fn summary<W: Write>(&self, mut writer: W) -> std::io::Result<()> {
        writeln!(&mut writer, "Summary Reassigned Token Account Report")?;
        writeln!(&mut writer, "Status,Account Address,Owner Address,Set Owner Signature,Delegation Signature,Possibly Fraudulent Transfer and Burn Signatures")?;
        for (account_address, account_entry) in &self.entries_by_token_address {
            if account_entry.owner_changes.is_empty() {
                // no owner changes ever, we're safe!
                writeln!(
                    &mut writer,
                    "Safe,{},{},,,",
                    account_address, account_entry.current_owner
                )?;
            } else {
                // Make a separate entry for each owner change
                // Note: this may show false positives if there are multiple
                // owner changes
                for owner_change in &account_entry.owner_changes {
                    // check for any delegations *before* the owner change
                    let mut line_has_been_printed = false;
                    for delegate_change in &account_entry.delegate_changes {
                        // uh oh, the delegate was changed before the owner change
                        if delegate_change.slot <= owner_change.slot {
                            let delegate = delegate_change.new_delegate;

                            // let's find all transfers and burns by this key, that's most likely fraud
                            let mut fraudulent_transactions = vec![];
                            for burn in &account_entry.possible_delegate_burns {
                                if burn.slot >= owner_change.slot && burn.signer == delegate {
                                    fraudulent_transactions
                                        .push(format!("{}", burn.transaction_id));
                                }
                            }
                            for transfer in &account_entry.possible_delegate_transfers {
                                if transfer.slot >= owner_change.slot && transfer.signer == delegate
                                {
                                    fraudulent_transactions
                                        .push(format!("{}", transfer.transaction_id));
                                }
                            }

                            if fraudulent_transactions.is_empty() {
                                // no fraud yet, but *must* clear delegation if present
                                writeln!(
                                    &mut writer,
                                    "Warning - clear delegation immediately,{},{},{},{},",
                                    account_address,
                                    account_entry.current_owner,
                                    owner_change.transaction_id,
                                    delegate_change.transaction_id
                                )?;
                            } else {
                                // oh no, some fraud most likely
                                writeln!(
                                    &mut writer,
                                    "Danger - possible fraud,{},{},{},{},{}",
                                    account_address,
                                    account_entry.current_owner,
                                    owner_change.transaction_id,
                                    delegate_change.transaction_id,
                                    fraudulent_transactions.join(" ")
                                )?;
                            }
                            line_has_been_printed = true;
                        }
                    }

                    if !line_has_been_printed {
                        // a reassignment was done, but no delegations, should be fine!
                        writeln!(
                            &mut writer,
                            "Safe - reassignment only,{},{},{},,",
                            account_address,
                            account_entry.current_owner,
                            owner_change.transaction_id
                        )?;
                    }
                }
            }
        }
        Ok(())
    }

    pub fn detail<W: Write>(&self, mut writer: W) -> std::io::Result<()> {
        writeln!(&mut writer, "Detailed Reassigned Token Account Report")?;
        writeln!(&mut writer)?;
        writeln!(&mut writer, "Owner Reassignment Transactions")?;
        writeln!(
            &mut writer,
            "Account Address,Owner,Signature,Slot,Previous Owner,New Owner,JSON Instruction"
        )?;
        for (account_address, account_entry) in &self.entries_by_token_address {
            for owner_change in &account_entry.owner_changes {
                writeln!(
                    &mut writer,
                    "{},{},{},{},{},{},{}",
                    account_address,
                    account_entry.current_owner,
                    owner_change.transaction_id,
                    owner_change.slot,
                    owner_change.signer,
                    owner_change.new_owner,
                    owner_change.original_ix
                )?;
            }
        }
        writeln!(&mut writer)?;
        writeln!(&mut writer, "Delegation Change Transactions")?;
        writeln!(
            &mut writer,
            "Account Address,Owner,Signature,Slot,Owner,Delegate,JSON Instruction"
        )?;
        for (account_address, account_entry) in &self.entries_by_token_address {
            for delegate_change in &account_entry.delegate_changes {
                writeln!(
                    &mut writer,
                    "{},{},{},{},{},{},{}",
                    account_address,
                    account_entry.current_owner,
                    delegate_change.transaction_id,
                    delegate_change.slot,
                    delegate_change.signer,
                    delegate_change.new_delegate,
                    delegate_change.original_ix
                )?;
            }
        }
        writeln!(&mut writer)?;
        writeln!(&mut writer, "Possibly Fraudulent Transfers")?;
        writeln!(
            &mut writer,
            "Account Address,Owner,Signature,Slot,Signer,Amount,JSON Instruction"
        )?;
        for (account_address, account_entry) in &self.entries_by_token_address {
            for transfer in &account_entry.possible_delegate_transfers {
                writeln!(
                    &mut writer,
                    "{},{},{},{},{},{},{}",
                    account_address,
                    account_entry.current_owner,
                    transfer.transaction_id,
                    transfer.slot,
                    transfer.signer,
                    transfer.amount,
                    transfer.original_ix
                )?;
            }
        }

        writeln!(&mut writer)?;
        writeln!(&mut writer, "Possibly Fraudulent Burns")?;
        writeln!(
            &mut writer,
            "Account Address,Owner,Signature,Slot,Signer,Amount,JSON Instruction"
        )?;
        for (account_address, account_entry) in &self.entries_by_token_address {
            for burn in &account_entry.possible_delegate_burns {
                writeln!(
                    &mut writer,
                    "{},{},{},{},{},{},{}",
                    account_address,
                    account_entry.current_owner,
                    burn.transaction_id,
                    burn.slot,
                    burn.signer,
                    burn.amount,
                    burn.original_ix
                )?;
            }
        }
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::token::{DelegateBurn, DelegateChange, DelegateTransfer, OwnerChange};
    use solana_sdk::{clock::Slot, signature::Signature, signer::keypair::Keypair};

    fn new_signature() -> Signature {
        let keypair = Keypair::new();
        Signature::new(&keypair.to_bytes())
    }

    fn new_delegate_transfer(slot: Slot) -> DelegateTransfer {
        DelegateTransfer {
            slot,
            transaction_id: new_signature(),
            signer: Pubkey::new_unique(),
            amount: "100".to_string(),
            original_ix: "ix".to_string(),
        }
    }

    fn new_delegate_burn(slot: Slot) -> DelegateBurn {
        DelegateBurn {
            slot,
            transaction_id: new_signature(),
            signer: Pubkey::new_unique(),
            amount: "100".to_string(),
            original_ix: "ix".to_string(),
        }
    }

    fn new_owner_change(slot: Slot) -> OwnerChange {
        OwnerChange {
            slot,
            transaction_id: new_signature(),
            signer: Pubkey::new_unique(),
            new_owner: Pubkey::new_unique(),
            original_ix: "ix".to_string(),
        }
    }

    fn new_delegate_change(slot: Slot) -> DelegateChange {
        DelegateChange {
            slot,
            transaction_id: new_signature(),
            signer: Pubkey::new_unique(),
            new_delegate: Pubkey::new_unique(),
            original_ix: "ix".to_string(),
        }
    }

    /// A good token account entry has no owner changes ever
    fn good_token_account_entry(owner: Pubkey, mint: Pubkey) -> TokenAccountEntry {
        let mut token_account_entry = TokenAccountEntry::new(owner, mint);
        let slot = 10;
        token_account_entry
            .possible_delegate_transfers
            .push(new_delegate_transfer(slot));
        token_account_entry
            .possible_delegate_burns
            .push(new_delegate_burn(slot));
        token_account_entry
            .delegate_changes
            .push(new_delegate_change(slot));
        token_account_entry
            .all_delegate_addresses
            .insert(Pubkey::new_unique());
        token_account_entry
    }

    /// A reassigned account entry has had its ownership changed
    fn reassigned_token_account_entry(owner: Pubkey, mint: Pubkey) -> TokenAccountEntry {
        let mut token_account_entry = TokenAccountEntry::new(owner, mint);
        let slot = 10;
        // only an owner change
        token_account_entry
            .owner_changes
            .push(new_owner_change(slot));
        token_account_entry
    }

    /// An open delegation account entry has a delegation set by a previous owner
    fn open_delegation_token_account_entry(owner: Pubkey, mint: Pubkey) -> TokenAccountEntry {
        let mut token_account_entry = TokenAccountEntry::new(owner, mint);
        let slot = 10;
        // no delegate transfers or burns, but previous owner delegated
        token_account_entry
            .owner_changes
            .push(new_owner_change(slot));
        token_account_entry
            .delegate_changes
            .push(new_delegate_change(slot));
        token_account_entry
            .all_delegate_addresses
            .insert(Pubkey::new_unique());
        token_account_entry
    }

    /// Fraudulent account entry has a delegation set by a previous owner who
    /// signed transfers and / or burns
    fn fraudulent_token_account_entry(owner: Pubkey, mint: Pubkey) -> TokenAccountEntry {
        let mut token_account_entry = TokenAccountEntry::new(owner, mint);
        let slot = 10;
        token_account_entry
            .owner_changes
            .push(new_owner_change(slot));
        let delegate_change = new_delegate_change(slot);
        let mut delegate_transfer = new_delegate_transfer(slot);
        delegate_transfer.signer = delegate_change.new_delegate;
        token_account_entry
            .possible_delegate_transfers
            .push(delegate_transfer);
        let mut delegate_burn = new_delegate_burn(slot);
        delegate_burn.signer = delegate_change.new_delegate;
        token_account_entry
            .possible_delegate_burns
            .push(delegate_burn);
        token_account_entry
            .all_delegate_addresses
            .insert(delegate_change.new_delegate);
        token_account_entry.delegate_changes.push(delegate_change);
        token_account_entry
    }

    #[test]
    fn detail_good() {
        let owner = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let entry = good_token_account_entry(owner, mint);
        let mut report = Report::new();
        report.entries_by_token_address.insert(owner, entry);
        let mut buffer: Vec<u8> = vec![];
        report.detail(&mut buffer).unwrap();
        let converted = std::str::from_utf8(&buffer).unwrap();
        println!("{}", converted);
    }

    #[test]
    fn detail_reassigned() {
        let owner = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let entry = reassigned_token_account_entry(owner, mint);
        let mut report = Report::new();
        report.entries_by_token_address.insert(owner, entry);
        let mut buffer: Vec<u8> = vec![];
        report.detail(&mut buffer).unwrap();
        let converted = std::str::from_utf8(&buffer).unwrap();
        println!("{}", converted);
    }

    #[test]
    fn detail_open_delegation() {
        let owner = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let entry = open_delegation_token_account_entry(owner, mint);
        let mut report = Report::new();
        report.entries_by_token_address.insert(owner, entry);
        let mut buffer: Vec<u8> = vec![];
        report.detail(&mut buffer).unwrap();
        let converted = std::str::from_utf8(&buffer).unwrap();
        println!("{}", converted);
    }

    #[test]
    fn detail_fraudulent() {
        let owner = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let entry = fraudulent_token_account_entry(owner, mint);
        let mut report = Report::new();
        report.entries_by_token_address.insert(owner, entry);
        let mut buffer: Vec<u8> = vec![];
        report.detail(&mut buffer).unwrap();
        let converted = std::str::from_utf8(&buffer).unwrap();
        println!("{}", converted);
    }

    #[test]
    fn summary_good() {
        let owner = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let entry = good_token_account_entry(owner, mint);
        let mut report = Report::new();
        report.entries_by_token_address.insert(owner, entry);
        let mut buffer: Vec<u8> = vec![];
        report.summary(&mut buffer).unwrap();
        let converted = std::str::from_utf8(&buffer).unwrap();
        println!("{}", converted);
    }

    #[test]
    fn summary_reassigned() {
        let owner = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let entry = reassigned_token_account_entry(owner, mint);
        let mut report = Report::new();
        report.entries_by_token_address.insert(owner, entry);
        let mut buffer: Vec<u8> = vec![];
        report.summary(&mut buffer).unwrap();
        let converted = std::str::from_utf8(&buffer).unwrap();
        println!("{}", converted);
    }

    #[test]
    fn summary_open_delegation() {
        let owner = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let entry = open_delegation_token_account_entry(owner, mint);
        let mut report = Report::new();
        report.entries_by_token_address.insert(owner, entry);
        let mut buffer: Vec<u8> = vec![];
        report.summary(&mut buffer).unwrap();
        let converted = std::str::from_utf8(&buffer).unwrap();
        println!("{}", converted);
    }

    #[test]
    fn summary_fraudulent() {
        let owner = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let entry = fraudulent_token_account_entry(owner, mint);
        let mut report = Report::new();
        report.entries_by_token_address.insert(owner, entry);
        let mut buffer: Vec<u8> = vec![];
        report.summary(&mut buffer).unwrap();
        let converted = std::str::from_utf8(&buffer).unwrap();
        println!("{}", converted);
    }
}


