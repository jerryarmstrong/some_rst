test/actions/redeemParticipationBidV3.test.ts
=============================================

Last edited: 2022-06-14 09:19:26

Contents:

.. code-block:: ts

    import {
  NonWinningConstraint,
  ParticipationConfigV2,
  WinningConstraint,
} from '@metaplex-foundation/mpl-metaplex';
import { isEligibleForParticipationPrize } from '../../src/actions';

describe('redeem participation bid v3', () => {
  describe('isEligibleForParticipationPrize', () => {
    test('winIndex = null, winnerConstraint = NoParticipationPrize, nonWinningConstraint = NoParticipationPrize', () => {
      const result = isEligibleForParticipationPrize(null, {
        winnerConstraint: WinningConstraint.NoParticipationPrize,
        nonWinningConstraint: NonWinningConstraint.NoParticipationPrize,
      } as ParticipationConfigV2);
      expect(result).toBe(false);
    });

    test('winIndex = null, winnerConstraint = ParticipationPrizeGiven, nonWinningConstraint = NoParticipationPrize', () => {
      const result = isEligibleForParticipationPrize(null, {
        winnerConstraint: WinningConstraint.ParticipationPrizeGiven,
        nonWinningConstraint: NonWinningConstraint.NoParticipationPrize,
      } as ParticipationConfigV2);
      expect(result).toBe(false);
    });

    test('winIndex = null, winnerConstraint = NoParticipationPrize, nonWinningConstraint = GivenForFixedPrice', () => {
      const result = isEligibleForParticipationPrize(null, {
        winnerConstraint: WinningConstraint.NoParticipationPrize,
        nonWinningConstraint: NonWinningConstraint.GivenForFixedPrice,
      } as ParticipationConfigV2);
      expect(result).toBe(true);
    });

    test('winIndex = null, winnerConstraint = ParticipationPrizeGiven, nonWinningConstraint = GivenForFixedPrice', () => {
      const result = isEligibleForParticipationPrize(null, {
        winnerConstraint: WinningConstraint.ParticipationPrizeGiven,
        nonWinningConstraint: NonWinningConstraint.GivenForFixedPrice,
      } as ParticipationConfigV2);
      expect(result).toBe(true);
    });

    test('winIndex = 0, winnerConstraint = NoParticipationPrize, nonWinningConstraint = NoParticipationPrize', () => {
      const result = isEligibleForParticipationPrize(0, {
        winnerConstraint: WinningConstraint.NoParticipationPrize,
        nonWinningConstraint: NonWinningConstraint.NoParticipationPrize,
      } as ParticipationConfigV2);
      expect(result).toBe(false);
    });

    test('winIndex = 0, winnerConstraint = ParticipationPrizeGiven, nonWinningConstraint = NoParticipationPrize', () => {
      const result = isEligibleForParticipationPrize(0, {
        winnerConstraint: WinningConstraint.ParticipationPrizeGiven,
        nonWinningConstraint: NonWinningConstraint.NoParticipationPrize,
      } as ParticipationConfigV2);
      expect(result).toBe(true);
    });

    test('winIndex = 0, winnerConstraint = NoParticipationPrize, nonWinningConstraint = GivenForFixedPrice', () => {
      const result = isEligibleForParticipationPrize(0, {
        winnerConstraint: WinningConstraint.NoParticipationPrize,
        nonWinningConstraint: NonWinningConstraint.GivenForFixedPrice,
      } as ParticipationConfigV2);
      expect(result).toBe(false);
    });

    test('winIndex = 0, winnerConstraint = ParticipationPrizeGiven, nonWinningConstraint = GivenForFixedPrice', () => {
      const result = isEligibleForParticipationPrize(null, {
        winnerConstraint: WinningConstraint.ParticipationPrizeGiven,
        nonWinningConstraint: NonWinningConstraint.GivenForFixedPrice,
      } as ParticipationConfigV2);
      expect(result).toBe(true);
    });
  });
});


