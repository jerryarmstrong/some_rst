saf/src/constraints.rs
======================

Last edited: 2022-11-28 20:53:26

Contents:

.. code-block:: rs

    use solana_address_lookup_table_program;
use solana_program::pubkey::Pubkey;

#[derive(Default)]
pub struct Constraints<'action> {
    pub seeds: Option<&'action [&'action [u8]]>,
    pub program_id: Option<Pubkey>,
    pub key_equals: Option<Pubkey>,
    pub writable: bool,
    pub signer: bool,
    pub program: bool,
    pub empty: bool,
    pub owned_by: Option<Pubkey>,
    pub first_byte_must_be: Option<u8>,
}

impl<'action> Constraints<'action> {
    pub fn new() -> Self {
        Constraints::default()
    }

    pub fn seeds(&mut self, seeds: &'action [&'action [u8]]) -> &mut Constraints<'action> {
        self.seeds = Some(seeds);
        self
    }

    pub fn program_id(&mut self, program_id: Pubkey) -> &mut Constraints<'action> {
        self.program_id = Some(program_id);
        self
    }

    pub fn signer(&mut self) -> &mut Constraints<'action> {
        self.signer = true;
        self
    }

    pub fn empty(&mut self) -> &mut Constraints<'action> {
        self.empty = true;
        self
    }

    pub fn first_byte(&mut self, byte: u8) -> &mut Constraints<'action> {
        self.first_byte_must_be = Some(byte);
        self
    }

    pub fn program(&mut self) -> &mut Constraints<'action> {
        self.program = true;
        self
    }

    pub fn writable(&mut self) -> &mut Constraints<'action> {
        self.writable = true;
        self
    }

    pub fn pubkey_equals(&mut self, pubkey: Pubkey) -> &mut Constraints<'action> {
        self.key_equals = Some(pubkey);
        self
    }

    pub fn owned_by(&mut self, pubkey: Pubkey) -> &mut Constraints<'action> {
        self.owned_by = Some(pubkey);
        self
    }

    pub fn pda(
        seeds: &'action [&'action [u8]],
        program_id: Pubkey,
        write: bool,
        empty: bool,
    ) -> Self {
        Constraints {
            seeds: Some(seeds),
            program_id: Some(program_id),
            key_equals: None,
            writable: write,
            signer: false,
            program: false,
            empty,
            owned_by: None,
            first_byte_must_be: None,
        }
    }

    pub fn system_program() -> Self {
        Constraints {
            seeds: None,
            program_id: None,
            key_equals: Some(solana_program::system_program::id()),
            writable: false,
            signer: false,
            program: true,
            empty: false,
            owned_by: None,
            first_byte_must_be: None,
        }
    }

    pub fn rent() -> Self {
        Constraints {
            seeds: None,
            program_id: None,
            key_equals: Some(solana_program::sysvar::rent::id()),
            writable: false,
            signer: false,
            program: true,
            empty: false,
            owned_by: None,
            first_byte_must_be: None,
        }
    }

    pub fn address_lookup_program() -> Self {
        Constraints {
            seeds: None,
            program_id: None,
            key_equals: Some(solana_address_lookup_table_program::id()),
            writable: false,
            signer: false,
            program: true,
            empty: false,
            owned_by: None,
            first_byte_must_be: None,
        }
    }

    pub fn read_only() -> Self {
        Constraints {
            seeds: None,
            program_id: None,
            key_equals: None,
            writable: false,
            signer: false,
            program: false,
            empty: false,
            owned_by: None,
            first_byte_must_be: None,
        }
    }

    pub fn read_only_optional_signer() -> Self {
        Constraints {
            seeds: None,
            program_id: None,
            key_equals: None,
            writable: false,
            signer: false,
            program: false,
            empty: false,
            owned_by: None,
            first_byte_must_be: None,
        }
    }

    pub fn payer() -> Self {
        Constraints {
            seeds: None,
            program_id: None,
            key_equals: None,
            writable: true,
            signer: true,
            program: false,
            empty: false,
            owned_by: None,
            first_byte_must_be: None,
        }
    }
}

#[cfg(test)]
mod tests {
    
    use crate::Constraints;
    use solana_program::pubkey::Pubkey;

    #[test]
    fn setup_works() {
        let owner = Pubkey::new_unique();
        let mut conn = Constraints::new();
        let con = conn.owned_by(owner).first_byte(4);
        assert_eq!(con.first_byte_must_be, Some(4));
        assert_eq!(con.owned_by, Some(owner));
    }
}


