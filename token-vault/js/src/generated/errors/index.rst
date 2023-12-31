token-vault/js/src/generated/errors/index.ts
============================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

type ErrorWithCode = Error & { code: number };
type MaybeErrorWithCode = ErrorWithCode | null | undefined;

const createErrorFromCodeLookup: Map<number, () => ErrorWithCode> = new Map();
const createErrorFromNameLookup: Map<string, () => ErrorWithCode> = new Map();

/**
 * InstructionUnpackError: 'Failed to unpack instruction data'
 *
 * @category Errors
 * @category generated
 */
export class InstructionUnpackErrorError extends Error {
  readonly code: number = 0x0;
  readonly name: string = 'InstructionUnpackError';
  constructor() {
    super('Failed to unpack instruction data');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, InstructionUnpackErrorError);
    }
  }
}

createErrorFromCodeLookup.set(0x0, () => new InstructionUnpackErrorError());
createErrorFromNameLookup.set('InstructionUnpackError', () => new InstructionUnpackErrorError());

/**
 * NotRentExempt: 'Lamport balance below rent-exempt threshold'
 *
 * @category Errors
 * @category generated
 */
export class NotRentExemptError extends Error {
  readonly code: number = 0x1;
  readonly name: string = 'NotRentExempt';
  constructor() {
    super('Lamport balance below rent-exempt threshold');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, NotRentExemptError);
    }
  }
}

createErrorFromCodeLookup.set(0x1, () => new NotRentExemptError());
createErrorFromNameLookup.set('NotRentExempt', () => new NotRentExemptError());

/**
 * AlreadyInitialized: 'Already initialized'
 *
 * @category Errors
 * @category generated
 */
export class AlreadyInitializedError extends Error {
  readonly code: number = 0x2;
  readonly name: string = 'AlreadyInitialized';
  constructor() {
    super('Already initialized');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, AlreadyInitializedError);
    }
  }
}

createErrorFromCodeLookup.set(0x2, () => new AlreadyInitializedError());
createErrorFromNameLookup.set('AlreadyInitialized', () => new AlreadyInitializedError());

/**
 * Uninitialized: 'Uninitialized'
 *
 * @category Errors
 * @category generated
 */
export class UninitializedError extends Error {
  readonly code: number = 0x3;
  readonly name: string = 'Uninitialized';
  constructor() {
    super('Uninitialized');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, UninitializedError);
    }
  }
}

createErrorFromCodeLookup.set(0x3, () => new UninitializedError());
createErrorFromNameLookup.set('Uninitialized', () => new UninitializedError());

/**
 * IncorrectOwner: 'Account does not have correct owner'
 *
 * @category Errors
 * @category generated
 */
export class IncorrectOwnerError extends Error {
  readonly code: number = 0x4;
  readonly name: string = 'IncorrectOwner';
  constructor() {
    super('Account does not have correct owner');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, IncorrectOwnerError);
    }
  }
}

createErrorFromCodeLookup.set(0x4, () => new IncorrectOwnerError());
createErrorFromNameLookup.set('IncorrectOwner', () => new IncorrectOwnerError());

/**
 * NumericalOverflowError: 'NumericalOverflowError'
 *
 * @category Errors
 * @category generated
 */
export class NumericalOverflowErrorError extends Error {
  readonly code: number = 0x5;
  readonly name: string = 'NumericalOverflowError';
  constructor() {
    super('NumericalOverflowError');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, NumericalOverflowErrorError);
    }
  }
}

createErrorFromCodeLookup.set(0x5, () => new NumericalOverflowErrorError());
createErrorFromNameLookup.set('NumericalOverflowError', () => new NumericalOverflowErrorError());

/**
 * TokenAccountContainsNoTokens: 'Provided token account contains no tokens'
 *
 * @category Errors
 * @category generated
 */
export class TokenAccountContainsNoTokensError extends Error {
  readonly code: number = 0x6;
  readonly name: string = 'TokenAccountContainsNoTokens';
  constructor() {
    super('Provided token account contains no tokens');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, TokenAccountContainsNoTokensError);
    }
  }
}

createErrorFromCodeLookup.set(0x6, () => new TokenAccountContainsNoTokensError());
createErrorFromNameLookup.set(
  'TokenAccountContainsNoTokens',
  () => new TokenAccountContainsNoTokensError(),
);

/**
 * TokenAccountAmountLessThanAmountSpecified: 'Provided token account cannot provide amount specified'
 *
 * @category Errors
 * @category generated
 */
export class TokenAccountAmountLessThanAmountSpecifiedError extends Error {
  readonly code: number = 0x7;
  readonly name: string = 'TokenAccountAmountLessThanAmountSpecified';
  constructor() {
    super('Provided token account cannot provide amount specified');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, TokenAccountAmountLessThanAmountSpecifiedError);
    }
  }
}

createErrorFromCodeLookup.set(0x7, () => new TokenAccountAmountLessThanAmountSpecifiedError());
createErrorFromNameLookup.set(
  'TokenAccountAmountLessThanAmountSpecified',
  () => new TokenAccountAmountLessThanAmountSpecifiedError(),
);

/**
 * VaultAccountIsNotEmpty: 'Provided vault account contains is not empty'
 *
 * @category Errors
 * @category generated
 */
export class VaultAccountIsNotEmptyError extends Error {
  readonly code: number = 0x8;
  readonly name: string = 'VaultAccountIsNotEmpty';
  constructor() {
    super('Provided vault account contains is not empty');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultAccountIsNotEmptyError);
    }
  }
}

createErrorFromCodeLookup.set(0x8, () => new VaultAccountIsNotEmptyError());
createErrorFromNameLookup.set('VaultAccountIsNotEmpty', () => new VaultAccountIsNotEmptyError());

/**
 * VaultAccountIsNotOwnedByProgram: 'Provided vault account is not owned by program derived address with seed of prefix and program id'
 *
 * @category Errors
 * @category generated
 */
export class VaultAccountIsNotOwnedByProgramError extends Error {
  readonly code: number = 0x9;
  readonly name: string = 'VaultAccountIsNotOwnedByProgram';
  constructor() {
    super(
      'Provided vault account is not owned by program derived address with seed of prefix and program id',
    );
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultAccountIsNotOwnedByProgramError);
    }
  }
}

createErrorFromCodeLookup.set(0x9, () => new VaultAccountIsNotOwnedByProgramError());
createErrorFromNameLookup.set(
  'VaultAccountIsNotOwnedByProgram',
  () => new VaultAccountIsNotOwnedByProgramError(),
);

/**
 * SafetyDepositAddressInvalid: 'The provided safety deposit account address does not match the expected program derived address'
 *
 * @category Errors
 * @category generated
 */
export class SafetyDepositAddressInvalidError extends Error {
  readonly code: number = 0xa;
  readonly name: string = 'SafetyDepositAddressInvalid';
  constructor() {
    super(
      'The provided safety deposit account address does not match the expected program derived address',
    );
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, SafetyDepositAddressInvalidError);
    }
  }
}

createErrorFromCodeLookup.set(0xa, () => new SafetyDepositAddressInvalidError());
createErrorFromNameLookup.set(
  'SafetyDepositAddressInvalid',
  () => new SafetyDepositAddressInvalidError(),
);

/**
 * TokenTransferFailed: 'Token transfer failed'
 *
 * @category Errors
 * @category generated
 */
export class TokenTransferFailedError extends Error {
  readonly code: number = 0xb;
  readonly name: string = 'TokenTransferFailed';
  constructor() {
    super('Token transfer failed');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, TokenTransferFailedError);
    }
  }
}

createErrorFromCodeLookup.set(0xb, () => new TokenTransferFailedError());
createErrorFromNameLookup.set('TokenTransferFailed', () => new TokenTransferFailedError());

/**
 * TokenMintToFailed: 'Token mint to failed'
 *
 * @category Errors
 * @category generated
 */
export class TokenMintToFailedError extends Error {
  readonly code: number = 0xc;
  readonly name: string = 'TokenMintToFailed';
  constructor() {
    super('Token mint to failed');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, TokenMintToFailedError);
    }
  }
}

createErrorFromCodeLookup.set(0xc, () => new TokenMintToFailedError());
createErrorFromNameLookup.set('TokenMintToFailed', () => new TokenMintToFailedError());

/**
 * TokenBurnFailed: 'Token burn failed'
 *
 * @category Errors
 * @category generated
 */
export class TokenBurnFailedError extends Error {
  readonly code: number = 0xd;
  readonly name: string = 'TokenBurnFailed';
  constructor() {
    super('Token burn failed');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, TokenBurnFailedError);
    }
  }
}

createErrorFromCodeLookup.set(0xd, () => new TokenBurnFailedError());
createErrorFromNameLookup.set('TokenBurnFailed', () => new TokenBurnFailedError());

/**
 * VaultMintNotEmpty: 'Vault mint not empty on init'
 *
 * @category Errors
 * @category generated
 */
export class VaultMintNotEmptyError extends Error {
  readonly code: number = 0xe;
  readonly name: string = 'VaultMintNotEmpty';
  constructor() {
    super('Vault mint not empty on init');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultMintNotEmptyError);
    }
  }
}

createErrorFromCodeLookup.set(0xe, () => new VaultMintNotEmptyError());
createErrorFromNameLookup.set('VaultMintNotEmpty', () => new VaultMintNotEmptyError());

/**
 * VaultAuthorityNotProgram: 'Vault mint's authority not set to program PDA with seed of prefix and program id'
 *
 * @category Errors
 * @category generated
 */
export class VaultAuthorityNotProgramError extends Error {
  readonly code: number = 0xf;
  readonly name: string = 'VaultAuthorityNotProgram';
  constructor() {
    super("Vault mint's authority not set to program PDA with seed of prefix and program id");
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultAuthorityNotProgramError);
    }
  }
}

createErrorFromCodeLookup.set(0xf, () => new VaultAuthorityNotProgramError());
createErrorFromNameLookup.set(
  'VaultAuthorityNotProgram',
  () => new VaultAuthorityNotProgramError(),
);

/**
 * TreasuryNotEmpty: 'Vault treasury not empty on init'
 *
 * @category Errors
 * @category generated
 */
export class TreasuryNotEmptyError extends Error {
  readonly code: number = 0x10;
  readonly name: string = 'TreasuryNotEmpty';
  constructor() {
    super('Vault treasury not empty on init');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, TreasuryNotEmptyError);
    }
  }
}

createErrorFromCodeLookup.set(0x10, () => new TreasuryNotEmptyError());
createErrorFromNameLookup.set('TreasuryNotEmpty', () => new TreasuryNotEmptyError());

/**
 * TreasuryOwnerNotProgram: 'Vault treasury's owner not set to program pda with seed of prefix and program id'
 *
 * @category Errors
 * @category generated
 */
export class TreasuryOwnerNotProgramError extends Error {
  readonly code: number = 0x11;
  readonly name: string = 'TreasuryOwnerNotProgram';
  constructor() {
    super("Vault treasury's owner not set to program pda with seed of prefix and program id");
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, TreasuryOwnerNotProgramError);
    }
  }
}

createErrorFromCodeLookup.set(0x11, () => new TreasuryOwnerNotProgramError());
createErrorFromNameLookup.set('TreasuryOwnerNotProgram', () => new TreasuryOwnerNotProgramError());

/**
 * VaultShouldBeInactive: 'Vault should be inactive'
 *
 * @category Errors
 * @category generated
 */
export class VaultShouldBeInactiveError extends Error {
  readonly code: number = 0x12;
  readonly name: string = 'VaultShouldBeInactive';
  constructor() {
    super('Vault should be inactive');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultShouldBeInactiveError);
    }
  }
}

createErrorFromCodeLookup.set(0x12, () => new VaultShouldBeInactiveError());
createErrorFromNameLookup.set('VaultShouldBeInactive', () => new VaultShouldBeInactiveError());

/**
 * VaultShouldBeActive: 'Vault should be active'
 *
 * @category Errors
 * @category generated
 */
export class VaultShouldBeActiveError extends Error {
  readonly code: number = 0x13;
  readonly name: string = 'VaultShouldBeActive';
  constructor() {
    super('Vault should be active');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultShouldBeActiveError);
    }
  }
}

createErrorFromCodeLookup.set(0x13, () => new VaultShouldBeActiveError());
createErrorFromNameLookup.set('VaultShouldBeActive', () => new VaultShouldBeActiveError());

/**
 * VaultShouldBeCombined: 'Vault should be combined'
 *
 * @category Errors
 * @category generated
 */
export class VaultShouldBeCombinedError extends Error {
  readonly code: number = 0x14;
  readonly name: string = 'VaultShouldBeCombined';
  constructor() {
    super('Vault should be combined');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultShouldBeCombinedError);
    }
  }
}

createErrorFromCodeLookup.set(0x14, () => new VaultShouldBeCombinedError());
createErrorFromNameLookup.set('VaultShouldBeCombined', () => new VaultShouldBeCombinedError());

/**
 * VaultTreasuryMintDoesNotMatchVaultMint: 'Vault treasury needs to match fraction mint'
 *
 * @category Errors
 * @category generated
 */
export class VaultTreasuryMintDoesNotMatchVaultMintError extends Error {
  readonly code: number = 0x15;
  readonly name: string = 'VaultTreasuryMintDoesNotMatchVaultMint';
  constructor() {
    super('Vault treasury needs to match fraction mint');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultTreasuryMintDoesNotMatchVaultMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x15, () => new VaultTreasuryMintDoesNotMatchVaultMintError());
createErrorFromNameLookup.set(
  'VaultTreasuryMintDoesNotMatchVaultMint',
  () => new VaultTreasuryMintDoesNotMatchVaultMintError(),
);

/**
 * RedeemTreasuryCantShareSameMintAsFraction: 'Redeem Treasury cannot be same mint as fraction'
 *
 * @category Errors
 * @category generated
 */
export class RedeemTreasuryCantShareSameMintAsFractionError extends Error {
  readonly code: number = 0x16;
  readonly name: string = 'RedeemTreasuryCantShareSameMintAsFraction';
  constructor() {
    super('Redeem Treasury cannot be same mint as fraction');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, RedeemTreasuryCantShareSameMintAsFractionError);
    }
  }
}

createErrorFromCodeLookup.set(0x16, () => new RedeemTreasuryCantShareSameMintAsFractionError());
createErrorFromNameLookup.set(
  'RedeemTreasuryCantShareSameMintAsFraction',
  () => new RedeemTreasuryCantShareSameMintAsFractionError(),
);

/**
 * InvalidAuthority: 'Invalid program authority provided'
 *
 * @category Errors
 * @category generated
 */
export class InvalidAuthorityError extends Error {
  readonly code: number = 0x17;
  readonly name: string = 'InvalidAuthority';
  constructor() {
    super('Invalid program authority provided');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, InvalidAuthorityError);
    }
  }
}

createErrorFromCodeLookup.set(0x17, () => new InvalidAuthorityError());
createErrorFromNameLookup.set('InvalidAuthority', () => new InvalidAuthorityError());

/**
 * RedeemTreasuryMintMustMatchLookupMint: 'Redeem treasury mint must match lookup mint'
 *
 * @category Errors
 * @category generated
 */
export class RedeemTreasuryMintMustMatchLookupMintError extends Error {
  readonly code: number = 0x18;
  readonly name: string = 'RedeemTreasuryMintMustMatchLookupMint';
  constructor() {
    super('Redeem treasury mint must match lookup mint');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, RedeemTreasuryMintMustMatchLookupMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x18, () => new RedeemTreasuryMintMustMatchLookupMintError());
createErrorFromNameLookup.set(
  'RedeemTreasuryMintMustMatchLookupMint',
  () => new RedeemTreasuryMintMustMatchLookupMintError(),
);

/**
 * PaymentMintShouldMatchPricingMint: 'You must pay with the same mint as the external pricing oracle'
 *
 * @category Errors
 * @category generated
 */
export class PaymentMintShouldMatchPricingMintError extends Error {
  readonly code: number = 0x19;
  readonly name: string = 'PaymentMintShouldMatchPricingMint';
  constructor() {
    super('You must pay with the same mint as the external pricing oracle');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, PaymentMintShouldMatchPricingMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x19, () => new PaymentMintShouldMatchPricingMintError());
createErrorFromNameLookup.set(
  'PaymentMintShouldMatchPricingMint',
  () => new PaymentMintShouldMatchPricingMintError(),
);

/**
 * ShareMintShouldMatchFractionalMint: 'Your share account should match the mint of the fractional mint'
 *
 * @category Errors
 * @category generated
 */
export class ShareMintShouldMatchFractionalMintError extends Error {
  readonly code: number = 0x1a;
  readonly name: string = 'ShareMintShouldMatchFractionalMint';
  constructor() {
    super('Your share account should match the mint of the fractional mint');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, ShareMintShouldMatchFractionalMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x1a, () => new ShareMintShouldMatchFractionalMintError());
createErrorFromNameLookup.set(
  'ShareMintShouldMatchFractionalMint',
  () => new ShareMintShouldMatchFractionalMintError(),
);

/**
 * VaultMintNeedsToMatchVault: 'Vault mint provided does not match that on the token vault'
 *
 * @category Errors
 * @category generated
 */
export class VaultMintNeedsToMatchVaultError extends Error {
  readonly code: number = 0x1b;
  readonly name: string = 'VaultMintNeedsToMatchVault';
  constructor() {
    super('Vault mint provided does not match that on the token vault');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultMintNeedsToMatchVaultError);
    }
  }
}

createErrorFromCodeLookup.set(0x1b, () => new VaultMintNeedsToMatchVaultError());
createErrorFromNameLookup.set(
  'VaultMintNeedsToMatchVault',
  () => new VaultMintNeedsToMatchVaultError(),
);

/**
 * RedeemTreasuryNeedsToMatchVault: 'Redeem treasury provided does not match that on the token vault'
 *
 * @category Errors
 * @category generated
 */
export class RedeemTreasuryNeedsToMatchVaultError extends Error {
  readonly code: number = 0x1c;
  readonly name: string = 'RedeemTreasuryNeedsToMatchVault';
  constructor() {
    super('Redeem treasury provided does not match that on the token vault');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, RedeemTreasuryNeedsToMatchVaultError);
    }
  }
}

createErrorFromCodeLookup.set(0x1c, () => new RedeemTreasuryNeedsToMatchVaultError());
createErrorFromNameLookup.set(
  'RedeemTreasuryNeedsToMatchVault',
  () => new RedeemTreasuryNeedsToMatchVaultError(),
);

/**
 * FractionTreasuryNeedsToMatchVault: 'Fraction treasury provided does not match that on the token vault'
 *
 * @category Errors
 * @category generated
 */
export class FractionTreasuryNeedsToMatchVaultError extends Error {
  readonly code: number = 0x1d;
  readonly name: string = 'FractionTreasuryNeedsToMatchVault';
  constructor() {
    super('Fraction treasury provided does not match that on the token vault');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, FractionTreasuryNeedsToMatchVaultError);
    }
  }
}

createErrorFromCodeLookup.set(0x1d, () => new FractionTreasuryNeedsToMatchVaultError());
createErrorFromNameLookup.set(
  'FractionTreasuryNeedsToMatchVault',
  () => new FractionTreasuryNeedsToMatchVaultError(),
);

/**
 * NotAllowedToCombine: 'Not allowed to combine at this time'
 *
 * @category Errors
 * @category generated
 */
export class NotAllowedToCombineError extends Error {
  readonly code: number = 0x1e;
  readonly name: string = 'NotAllowedToCombine';
  constructor() {
    super('Not allowed to combine at this time');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, NotAllowedToCombineError);
    }
  }
}

createErrorFromCodeLookup.set(0x1e, () => new NotAllowedToCombineError());
createErrorFromNameLookup.set('NotAllowedToCombine', () => new NotAllowedToCombineError());

/**
 * CannotAffordToCombineThisVault: 'You cannot afford to combine this vault'
 *
 * @category Errors
 * @category generated
 */
export class CannotAffordToCombineThisVaultError extends Error {
  readonly code: number = 0x1f;
  readonly name: string = 'CannotAffordToCombineThisVault';
  constructor() {
    super('You cannot afford to combine this vault');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, CannotAffordToCombineThisVaultError);
    }
  }
}

createErrorFromCodeLookup.set(0x1f, () => new CannotAffordToCombineThisVaultError());
createErrorFromNameLookup.set(
  'CannotAffordToCombineThisVault',
  () => new CannotAffordToCombineThisVaultError(),
);

/**
 * NoShares: 'You have no shares to redeem'
 *
 * @category Errors
 * @category generated
 */
export class NoSharesError extends Error {
  readonly code: number = 0x20;
  readonly name: string = 'NoShares';
  constructor() {
    super('You have no shares to redeem');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, NoSharesError);
    }
  }
}

createErrorFromCodeLookup.set(0x20, () => new NoSharesError());
createErrorFromNameLookup.set('NoShares', () => new NoSharesError());

/**
 * OutstandingShareAccountNeedsToMatchFractionalMint: 'Your outstanding share account is the incorrect mint'
 *
 * @category Errors
 * @category generated
 */
export class OutstandingShareAccountNeedsToMatchFractionalMintError extends Error {
  readonly code: number = 0x21;
  readonly name: string = 'OutstandingShareAccountNeedsToMatchFractionalMint';
  constructor() {
    super('Your outstanding share account is the incorrect mint');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, OutstandingShareAccountNeedsToMatchFractionalMintError);
    }
  }
}

createErrorFromCodeLookup.set(
  0x21,
  () => new OutstandingShareAccountNeedsToMatchFractionalMintError(),
);
createErrorFromNameLookup.set(
  'OutstandingShareAccountNeedsToMatchFractionalMint',
  () => new OutstandingShareAccountNeedsToMatchFractionalMintError(),
);

/**
 * DestinationAccountNeedsToMatchRedeemMint: 'Your destination account is the incorrect mint'
 *
 * @category Errors
 * @category generated
 */
export class DestinationAccountNeedsToMatchRedeemMintError extends Error {
  readonly code: number = 0x22;
  readonly name: string = 'DestinationAccountNeedsToMatchRedeemMint';
  constructor() {
    super('Your destination account is the incorrect mint');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, DestinationAccountNeedsToMatchRedeemMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x22, () => new DestinationAccountNeedsToMatchRedeemMintError());
createErrorFromNameLookup.set(
  'DestinationAccountNeedsToMatchRedeemMint',
  () => new DestinationAccountNeedsToMatchRedeemMintError(),
);

/**
 * FractionSupplyEmpty: 'Fractional mint is empty'
 *
 * @category Errors
 * @category generated
 */
export class FractionSupplyEmptyError extends Error {
  readonly code: number = 0x23;
  readonly name: string = 'FractionSupplyEmpty';
  constructor() {
    super('Fractional mint is empty');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, FractionSupplyEmptyError);
    }
  }
}

createErrorFromCodeLookup.set(0x23, () => new FractionSupplyEmptyError());
createErrorFromNameLookup.set('FractionSupplyEmpty', () => new FractionSupplyEmptyError());

/**
 * TokenProgramProvidedDoesNotMatchVault: 'Token Program Provided Needs To Match Vault'
 *
 * @category Errors
 * @category generated
 */
export class TokenProgramProvidedDoesNotMatchVaultError extends Error {
  readonly code: number = 0x24;
  readonly name: string = 'TokenProgramProvidedDoesNotMatchVault';
  constructor() {
    super('Token Program Provided Needs To Match Vault');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, TokenProgramProvidedDoesNotMatchVaultError);
    }
  }
}

createErrorFromCodeLookup.set(0x24, () => new TokenProgramProvidedDoesNotMatchVaultError());
createErrorFromNameLookup.set(
  'TokenProgramProvidedDoesNotMatchVault',
  () => new TokenProgramProvidedDoesNotMatchVaultError(),
);

/**
 * AuthorityIsNotSigner: 'Authority of vault needs to be signer for this action'
 *
 * @category Errors
 * @category generated
 */
export class AuthorityIsNotSignerError extends Error {
  readonly code: number = 0x25;
  readonly name: string = 'AuthorityIsNotSigner';
  constructor() {
    super('Authority of vault needs to be signer for this action');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, AuthorityIsNotSignerError);
    }
  }
}

createErrorFromCodeLookup.set(0x25, () => new AuthorityIsNotSignerError());
createErrorFromNameLookup.set('AuthorityIsNotSigner', () => new AuthorityIsNotSignerError());

/**
 * AuthorityDoesNotMatch: 'Authority of vault does not match authority provided'
 *
 * @category Errors
 * @category generated
 */
export class AuthorityDoesNotMatchError extends Error {
  readonly code: number = 0x26;
  readonly name: string = 'AuthorityDoesNotMatch';
  constructor() {
    super('Authority of vault does not match authority provided');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, AuthorityDoesNotMatchError);
    }
  }
}

createErrorFromCodeLookup.set(0x26, () => new AuthorityDoesNotMatchError());
createErrorFromNameLookup.set('AuthorityDoesNotMatch', () => new AuthorityDoesNotMatchError());

/**
 * SafetyDepositBoxVaultMismatch: 'This safety deposit box does not belong to this vault!'
 *
 * @category Errors
 * @category generated
 */
export class SafetyDepositBoxVaultMismatchError extends Error {
  readonly code: number = 0x27;
  readonly name: string = 'SafetyDepositBoxVaultMismatch';
  constructor() {
    super('This safety deposit box does not belong to this vault!');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, SafetyDepositBoxVaultMismatchError);
    }
  }
}

createErrorFromCodeLookup.set(0x27, () => new SafetyDepositBoxVaultMismatchError());
createErrorFromNameLookup.set(
  'SafetyDepositBoxVaultMismatch',
  () => new SafetyDepositBoxVaultMismatchError(),
);

/**
 * StoreDoesNotMatchSafetyDepositBox: 'The store provided does not match the store key on the safety deposit box!'
 *
 * @category Errors
 * @category generated
 */
export class StoreDoesNotMatchSafetyDepositBoxError extends Error {
  readonly code: number = 0x28;
  readonly name: string = 'StoreDoesNotMatchSafetyDepositBox';
  constructor() {
    super('The store provided does not match the store key on the safety deposit box!');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, StoreDoesNotMatchSafetyDepositBoxError);
    }
  }
}

createErrorFromCodeLookup.set(0x28, () => new StoreDoesNotMatchSafetyDepositBoxError());
createErrorFromNameLookup.set(
  'StoreDoesNotMatchSafetyDepositBox',
  () => new StoreDoesNotMatchSafetyDepositBoxError(),
);

/**
 * StoreEmpty: 'This safety deposit box is empty!'
 *
 * @category Errors
 * @category generated
 */
export class StoreEmptyError extends Error {
  readonly code: number = 0x29;
  readonly name: string = 'StoreEmpty';
  constructor() {
    super('This safety deposit box is empty!');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, StoreEmptyError);
    }
  }
}

createErrorFromCodeLookup.set(0x29, () => new StoreEmptyError());
createErrorFromNameLookup.set('StoreEmpty', () => new StoreEmptyError());

/**
 * DestinationAccountNeedsToMatchTokenMint: 'The destination account to receive your token needs to be the same mint as the token's mint'
 *
 * @category Errors
 * @category generated
 */
export class DestinationAccountNeedsToMatchTokenMintError extends Error {
  readonly code: number = 0x2a;
  readonly name: string = 'DestinationAccountNeedsToMatchTokenMint';
  constructor() {
    super(
      "The destination account to receive your token needs to be the same mint as the token's mint",
    );
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, DestinationAccountNeedsToMatchTokenMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x2a, () => new DestinationAccountNeedsToMatchTokenMintError());
createErrorFromNameLookup.set(
  'DestinationAccountNeedsToMatchTokenMint',
  () => new DestinationAccountNeedsToMatchTokenMintError(),
);

/**
 * DestinationAccountNeedsToMatchFractionMint: 'The destination account to receive your shares needs to be the same mint as the vault's fraction mint'
 *
 * @category Errors
 * @category generated
 */
export class DestinationAccountNeedsToMatchFractionMintError extends Error {
  readonly code: number = 0x2b;
  readonly name: string = 'DestinationAccountNeedsToMatchFractionMint';
  constructor() {
    super(
      "The destination account to receive your shares needs to be the same mint as the vault's fraction mint",
    );
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, DestinationAccountNeedsToMatchFractionMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x2b, () => new DestinationAccountNeedsToMatchFractionMintError());
createErrorFromNameLookup.set(
  'DestinationAccountNeedsToMatchFractionMint',
  () => new DestinationAccountNeedsToMatchFractionMintError(),
);

/**
 * SourceAccountNeedsToMatchFractionMint: 'The source account to send your shares from needs to be the same mint as the vault's fraction mint'
 *
 * @category Errors
 * @category generated
 */
export class SourceAccountNeedsToMatchFractionMintError extends Error {
  readonly code: number = 0x2c;
  readonly name: string = 'SourceAccountNeedsToMatchFractionMint';
  constructor() {
    super(
      "The source account to send your shares from needs to be the same mint as the vault's fraction mint",
    );
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, SourceAccountNeedsToMatchFractionMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x2c, () => new SourceAccountNeedsToMatchFractionMintError());
createErrorFromNameLookup.set(
  'SourceAccountNeedsToMatchFractionMint',
  () => new SourceAccountNeedsToMatchFractionMintError(),
);

/**
 * VaultDoesNotAllowNewShareMinting: 'This vault does not allow the minting of new shares!'
 *
 * @category Errors
 * @category generated
 */
export class VaultDoesNotAllowNewShareMintingError extends Error {
  readonly code: number = 0x2d;
  readonly name: string = 'VaultDoesNotAllowNewShareMinting';
  constructor() {
    super('This vault does not allow the minting of new shares!');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, VaultDoesNotAllowNewShareMintingError);
    }
  }
}

createErrorFromCodeLookup.set(0x2d, () => new VaultDoesNotAllowNewShareMintingError());
createErrorFromNameLookup.set(
  'VaultDoesNotAllowNewShareMinting',
  () => new VaultDoesNotAllowNewShareMintingError(),
);

/**
 * NotEnoughShares: 'There are not enough shares'
 *
 * @category Errors
 * @category generated
 */
export class NotEnoughSharesError extends Error {
  readonly code: number = 0x2e;
  readonly name: string = 'NotEnoughShares';
  constructor() {
    super('There are not enough shares');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, NotEnoughSharesError);
    }
  }
}

createErrorFromCodeLookup.set(0x2e, () => new NotEnoughSharesError());
createErrorFromNameLookup.set('NotEnoughShares', () => new NotEnoughSharesError());

/**
 * ExternalPriceAccountMustBeSigner: 'External price account must be signer'
 *
 * @category Errors
 * @category generated
 */
export class ExternalPriceAccountMustBeSignerError extends Error {
  readonly code: number = 0x2f;
  readonly name: string = 'ExternalPriceAccountMustBeSigner';
  constructor() {
    super('External price account must be signer');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, ExternalPriceAccountMustBeSignerError);
    }
  }
}

createErrorFromCodeLookup.set(0x2f, () => new ExternalPriceAccountMustBeSignerError());
createErrorFromNameLookup.set(
  'ExternalPriceAccountMustBeSigner',
  () => new ExternalPriceAccountMustBeSignerError(),
);

/**
 * RedeemTreasuryMintShouldMatchPricingMint: 'Very bad, someone changed external account's price mint after vault creation!'
 *
 * @category Errors
 * @category generated
 */
export class RedeemTreasuryMintShouldMatchPricingMintError extends Error {
  readonly code: number = 0x30;
  readonly name: string = 'RedeemTreasuryMintShouldMatchPricingMint';
  constructor() {
    super("Very bad, someone changed external account's price mint after vault creation!");
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, RedeemTreasuryMintShouldMatchPricingMintError);
    }
  }
}

createErrorFromCodeLookup.set(0x30, () => new RedeemTreasuryMintShouldMatchPricingMintError());
createErrorFromNameLookup.set(
  'RedeemTreasuryMintShouldMatchPricingMint',
  () => new RedeemTreasuryMintShouldMatchPricingMintError(),
);

/**
 * StoreLessThanAmount: 'Store has less than amount desired'
 *
 * @category Errors
 * @category generated
 */
export class StoreLessThanAmountError extends Error {
  readonly code: number = 0x31;
  readonly name: string = 'StoreLessThanAmount';
  constructor() {
    super('Store has less than amount desired');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, StoreLessThanAmountError);
    }
  }
}

createErrorFromCodeLookup.set(0x31, () => new StoreLessThanAmountError());
createErrorFromNameLookup.set('StoreLessThanAmount', () => new StoreLessThanAmountError());

/**
 * InvalidTokenProgram: 'Invalid token program'
 *
 * @category Errors
 * @category generated
 */
export class InvalidTokenProgramError extends Error {
  readonly code: number = 0x32;
  readonly name: string = 'InvalidTokenProgram';
  constructor() {
    super('Invalid token program');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, InvalidTokenProgramError);
    }
  }
}

createErrorFromCodeLookup.set(0x32, () => new InvalidTokenProgramError());
createErrorFromNameLookup.set('InvalidTokenProgram', () => new InvalidTokenProgramError());

/**
 * DataTypeMismatch: 'Data type mismatch'
 *
 * @category Errors
 * @category generated
 */
export class DataTypeMismatchError extends Error {
  readonly code: number = 0x33;
  readonly name: string = 'DataTypeMismatch';
  constructor() {
    super('Data type mismatch');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, DataTypeMismatchError);
    }
  }
}

createErrorFromCodeLookup.set(0x33, () => new DataTypeMismatchError());
createErrorFromNameLookup.set('DataTypeMismatch', () => new DataTypeMismatchError());

/**
 * DelegateShouldBeNone: 'Accept payment delegate should be none'
 *
 * @category Errors
 * @category generated
 */
export class DelegateShouldBeNoneError extends Error {
  readonly code: number = 0x34;
  readonly name: string = 'DelegateShouldBeNone';
  constructor() {
    super('Accept payment delegate should be none');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, DelegateShouldBeNoneError);
    }
  }
}

createErrorFromCodeLookup.set(0x34, () => new DelegateShouldBeNoneError());
createErrorFromNameLookup.set('DelegateShouldBeNone', () => new DelegateShouldBeNoneError());

/**
 * CloseAuthorityShouldBeNone: 'Accept payment close authority should be none'
 *
 * @category Errors
 * @category generated
 */
export class CloseAuthorityShouldBeNoneError extends Error {
  readonly code: number = 0x35;
  readonly name: string = 'CloseAuthorityShouldBeNone';
  constructor() {
    super('Accept payment close authority should be none');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, CloseAuthorityShouldBeNoneError);
    }
  }
}

createErrorFromCodeLookup.set(0x35, () => new CloseAuthorityShouldBeNoneError());
createErrorFromNameLookup.set(
  'CloseAuthorityShouldBeNone',
  () => new CloseAuthorityShouldBeNoneError(),
);

/**
 * DerivedKeyInvalid: 'Derived key invalid'
 *
 * @category Errors
 * @category generated
 */
export class DerivedKeyInvalidError extends Error {
  readonly code: number = 0x36;
  readonly name: string = 'DerivedKeyInvalid';
  constructor() {
    super('Derived key invalid');
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, DerivedKeyInvalidError);
    }
  }
}

createErrorFromCodeLookup.set(0x36, () => new DerivedKeyInvalidError());
createErrorFromNameLookup.set('DerivedKeyInvalid', () => new DerivedKeyInvalidError());

/**
 * Attempts to resolve a custom program error from the provided error code.
 * @category Errors
 * @category generated
 */
export function errorFromCode(code: number): MaybeErrorWithCode {
  const createError = createErrorFromCodeLookup.get(code);
  return createError != null ? createError() : null;
}

/**
 * Attempts to resolve a custom program error from the provided error name, i.e. 'Unauthorized'.
 * @category Errors
 * @category generated
 */
export function errorFromName(name: string): MaybeErrorWithCode {
  const createError = createErrorFromNameLookup.get(name);
  return createError != null ? createError() : null;
}


