clients/js/src/defaultGuards/freezeTokenPayment.ts
==================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import {
  TokenStandard,
  findMasterEditionPda,
  findMetadataPda,
  findTokenRecordPda,
  getMplTokenMetadataProgramId,
  isProgrammable,
} from '@metaplex-foundation/mpl-token-metadata';
import {
  findAssociatedTokenPda,
  getSplAssociatedTokenProgramId,
  getSplSystemProgramId,
  getSplTokenProgramId,
  getSysvar,
} from '@metaplex-foundation/mpl-toolbox';
import { PublicKey, Signer } from '@metaplex-foundation/umi';
import { tuple, u64 } from '@metaplex-foundation/umi/serializers';
import { UnrecognizePathForRouteInstructionError } from '../errors';
import {
  FreezeInstruction,
  FreezeTokenPayment,
  FreezeTokenPaymentArgs,
  findFreezeEscrowPda,
  getFreezeInstructionSerializer,
  getFreezeTokenPaymentSerializer,
} from '../generated';
import { GuardManifest, GuardRemainingAccount, RouteParser } from '../guards';
import { getMplTokenAuthRulesProgramId } from '../programs';

/**
 * The freezeTokenPayment guard allows minting frozen NFTs by charging
 * the payer a specific amount of tokens from a certain mint acount.
 * Frozen NFTs cannot be transferred or listed on any marketplaces until thawed.
 *
 * The funds are transferred to a freeze escrow until all NFTs are thaw,
 * at which point, they can be transferred (unlocked) to the configured
 * destination account.
 *
 * @see {@link FreezeTokenPaymentRouteArgs} to learn more about
 * the instructions that can be executed against this guard.
 */
export const freezeTokenPaymentGuardManifest: GuardManifest<
  FreezeTokenPaymentArgs,
  FreezeTokenPayment,
  FreezeTokenPaymentMintArgs,
  FreezeTokenPaymentRouteArgs
> = {
  name: 'freezeTokenPayment',
  serializer: getFreezeTokenPaymentSerializer,
  mintParser: (context, mintContext, args) => {
    const [freezeEscrow] = findFreezeEscrowPda(context, {
      destination: args.destinationAta,
      candyMachine: mintContext.candyMachine,
      candyGuard: mintContext.candyGuard,
    });
    const [nftAta] = findAssociatedTokenPda(context, {
      mint: mintContext.mint,
      owner: mintContext.minter.publicKey,
    });
    const [tokenAddress] = findAssociatedTokenPda(context, {
      mint: args.mint,
      owner: mintContext.minter.publicKey,
    });
    const [freezeAta] = findAssociatedTokenPda(context, {
      mint: args.mint,
      owner: freezeEscrow,
    });
    return {
      data: new Uint8Array(),
      remainingAccounts: [
        { publicKey: freezeEscrow, isWritable: true },
        { publicKey: nftAta, isWritable: false },
        { publicKey: tokenAddress, isWritable: true },
        { publicKey: freezeAta, isWritable: true },
        ...(args.nftRuleSet
          ? [{ publicKey: args.nftRuleSet, isWritable: false }]
          : []),
      ],
    };
  },
  routeParser: (context, routeContext, args) => {
    const { path } = args;
    switch (path) {
      case 'initialize':
        return initializeRouteInstruction(context, routeContext, args);
      case 'thaw':
        return thawRouteInstruction(context, routeContext, args);
      case 'unlockFunds':
        return unlockFundsRouteInstruction(context, routeContext, args);
      default:
        throw new UnrecognizePathForRouteInstructionError(
          'freezeTokenPayment',
          path
        );
    }
  },
};

export type FreezeTokenPaymentMintArgs = Omit<
  FreezeTokenPaymentArgs,
  'amount'
> & {
  /** The ruleSet of the minted NFT, if any. */
  nftRuleSet?: PublicKey;
};

/**
 * The settings for the freezeTokenPayment guard that should be provided
 * when accessing the guard's special "route" instruction.
 */
export type FreezeTokenPaymentRouteArgs =
  | FreezeTokenPaymentRouteArgsInitialize
  | FreezeTokenPaymentRouteArgsThaw
  | FreezeTokenPaymentRouteArgsUnlockFunds;

/**
 * The `initialize` path creates the freeze escrow account that will
 * hold the funds until all NFTs are thawed. It must be called before
 * any NFTs can be minted.
 *
 * ```ts
 * route(umi, {
 *   // ...
 *   guard: 'freezeTokenPayment',
 *   routeArgs: {
 *     path: 'initialize',
 *     mint: tokenMint.publicKey,
 *     destinationAta,
 *     period: 15 * 24 * 60 * 60, // 15 days.
 *     candyGuardAuthority,
 *   },
 * });
 * ```
 */
export type FreezeTokenPaymentRouteArgsInitialize = Omit<
  FreezeTokenPaymentArgs,
  'amount'
> & {
  /** Selects the path to execute in the route instruction. */
  path: 'initialize';

  /** The freeze period in seconds (maximum 30 days). */
  period: number;

  /** The authority of the Candy Guard as a Signer. */
  candyGuardAuthority: Signer;
};

/**
 * The `thaw` path unfreezes one NFT if one of the following conditions are met:
 * - All NFTs have been minted.
 * - The configured period has elapsed (max 30 days).
 * - The Candy Machine account was deleted.
 *
 * Anyone can call this instruction. Since the funds are not transferrable
 * until all NFTs are thawed, it creates an incentive for the treasury to
 * thaw all NFTs as soon as possible.
 *
 * ```ts
 * route(umi, {
 *   // ...
 *   guard: 'freezeTokenPayment',
 *   routeArgs: {
 *     path: 'thaw',
 *     mint: tokenMint.publicKey,
 *     destinationAta,
 *     nftMint,
 *     nftOwner,
 *     nftTokenStandard: candyMachine.tokenStandard,
 *   },
 * });
 * ```
 */
export type FreezeTokenPaymentRouteArgsThaw = Omit<
  FreezeTokenPaymentArgs,
  'amount'
> & {
  /** Selects the path to execute in the route instruction. */
  path: 'thaw';

  /** The mint address of the NFT to thaw. */
  nftMint: PublicKey;

  /** The owner address of the NFT to thaw. */
  nftOwner: PublicKey;

  /** The token standard of the minted NFT. */
  nftTokenStandard: TokenStandard;

  /** The ruleSet of the minted NFT, if any. */
  nftRuleSet?: PublicKey;
};

/**
 * The `unlockFunds` path transfers all of the escrow funds to the
 * configured destination token address once all NFTs have been thawed.
 *
 * ```ts
 * route(umi, {
 *   // ...
 *   guard: 'freezeTokenPayment',
 *   routeArgs: {
 *     path: 'unlockFunds',
 *     mint: tokenMint.publicKey,
 *     destinationAta,
 *     candyGuardAuthority,
 *   },
 * });
 * ```
 */
export type FreezeTokenPaymentRouteArgsUnlockFunds = Omit<
  FreezeTokenPaymentArgs,
  'amount'
> & {
  /** Selects the path to execute in the route instruction. */
  path: 'unlockFunds';

  /** The authority of the Candy Guard as a Signer. */
  candyGuardAuthority: Signer;
};

const initializeRouteInstruction: RouteParser<
  FreezeTokenPaymentRouteArgsInitialize
> = (context, routeContext, args) => {
  const [freezeEscrow] = findFreezeEscrowPda(context, {
    destination: args.destinationAta,
    candyMachine: routeContext.candyMachine,
    candyGuard: routeContext.candyGuard,
  });
  const [freezeAta] = findAssociatedTokenPda(context, {
    mint: args.mint,
    owner: freezeEscrow,
  });
  const serializer = tuple([getFreezeInstructionSerializer(), u64()]);
  return {
    data: serializer.serialize([FreezeInstruction.Initialize, args.period]),
    remainingAccounts: [
      { publicKey: freezeEscrow, isWritable: true },
      { signer: args.candyGuardAuthority, isWritable: false },
      { publicKey: getSplSystemProgramId(context), isWritable: false },
      { publicKey: freezeAta, isWritable: true },
      { publicKey: args.mint, isWritable: false },
      { publicKey: getSplTokenProgramId(context), isWritable: false },
      { publicKey: getSplAssociatedTokenProgramId(context), isWritable: false },
      { publicKey: args.destinationAta, isWritable: true },
    ],
  };
};

const thawRouteInstruction: RouteParser<FreezeTokenPaymentRouteArgsThaw> = (
  context,
  routeContext,
  args
) => {
  const [freezeEscrow] = findFreezeEscrowPda(context, {
    destination: args.destinationAta,
    candyMachine: routeContext.candyMachine,
    candyGuard: routeContext.candyGuard,
  });
  const [nftFreezeAta] = findAssociatedTokenPda(context, {
    mint: args.nftMint,
    owner: freezeEscrow,
  });
  const [nftAta] = findAssociatedTokenPda(context, {
    mint: args.nftMint,
    owner: args.nftOwner,
  });
  const [nftMetadata] = findMetadataPda(context, { mint: args.nftMint });
  const [nftEdition] = findMasterEditionPda(context, { mint: args.nftMint });
  const [nftAtaTokenRecord] = findTokenRecordPda(context, {
    mint: args.nftMint,
    token: nftAta,
  });
  const [nftFreezeAtaTokenRecord] = findTokenRecordPda(context, {
    mint: args.nftMint,
    token: nftFreezeAta,
  });
  const data = getFreezeInstructionSerializer(context).serialize(
    FreezeInstruction.Thaw
  );
  const remainingAccounts: GuardRemainingAccount[] = [
    { publicKey: freezeEscrow, isWritable: true },
    { publicKey: args.nftMint, isWritable: false },
    { publicKey: args.nftOwner, isWritable: false },
    { publicKey: nftAta, isWritable: true },
    { publicKey: nftEdition, isWritable: false },
    { publicKey: getSplTokenProgramId(context), isWritable: false },
    { publicKey: getMplTokenMetadataProgramId(context), isWritable: false },
  ];

  if (!isProgrammable(args.nftTokenStandard)) {
    return { data, remainingAccounts };
  }

  remainingAccounts.push(
    ...[
      { publicKey: nftMetadata, isWritable: true },
      { publicKey: nftFreezeAta, isWritable: true },
      { publicKey: getSplSystemProgramId(context), isWritable: false },
      { publicKey: getSysvar('instructions'), isWritable: false },
      { publicKey: getSplAssociatedTokenProgramId(context), isWritable: false },
      { publicKey: nftAtaTokenRecord, isWritable: true },
      { publicKey: nftFreezeAtaTokenRecord, isWritable: true },
    ]
  );

  if (args.nftRuleSet) {
    const tokenAuthRules = getMplTokenAuthRulesProgramId(context);
    remainingAccounts.push(
      ...[
        { publicKey: tokenAuthRules, isWritable: false },
        { publicKey: args.nftRuleSet, isWritable: false },
      ]
    );
  }

  return { data, remainingAccounts };
};

const unlockFundsRouteInstruction: RouteParser<
  FreezeTokenPaymentRouteArgsUnlockFunds
> = (context, routeContext, args) => {
  const [freezeEscrow] = findFreezeEscrowPda(context, {
    destination: args.destinationAta,
    candyMachine: routeContext.candyMachine,
    candyGuard: routeContext.candyGuard,
  });
  const [freezeAta] = findAssociatedTokenPda(context, {
    mint: args.mint,
    owner: freezeEscrow,
  });
  return {
    data: getFreezeInstructionSerializer(context).serialize(
      FreezeInstruction.UnlockFunds
    ),
    remainingAccounts: [
      { publicKey: freezeEscrow, isWritable: true },
      { signer: args.candyGuardAuthority, isWritable: false },
      { publicKey: freezeAta, isWritable: true },
      { publicKey: args.destinationAta, isWritable: true },
      { publicKey: getSplTokenProgramId(context), isWritable: false },
      { publicKey: getSplSystemProgramId(context), isWritable: false },
    ],
  };
};


