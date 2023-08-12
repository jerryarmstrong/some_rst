packages/addresses/src/program-derived-address.ts
=================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { assertDigestCapabilityIsAvailable } from '@solana/assertions';

import { Base58EncodedAddress, getBase58EncodedAddressCodec } from './base58';
import { compressedPointBytesAreOnCurve } from './curve';

type PDAInput = Readonly<{
    programAddress: Base58EncodedAddress;
    seeds: Seed[];
}>;
type Seed = string | Uint8Array;

const MAX_SEED_LENGTH = 32;
const MAX_SEEDS = 16;
const PDA_MARKER_BYTES = [
    // The string 'ProgramDerivedAddress'
    80, 114, 111, 103, 114, 97, 109, 68, 101, 114, 105, 118, 101, 100, 65, 100, 100, 114, 101, 115, 115,
] as const;

// TODO: Coded error.
class PointOnCurveError extends Error {}

async function createProgramDerivedAddress({ programAddress, seeds }: PDAInput): Promise<Base58EncodedAddress> {
    await assertDigestCapabilityIsAvailable();
    if (seeds.length > MAX_SEEDS) {
        // TODO: Coded error.
        throw new Error(`A maximum of ${MAX_SEEDS} seeds may be supplied when creating an address`);
    }
    let textEncoder: TextEncoder;
    const seedBytes = seeds.reduce((acc, seed, ii) => {
        const bytes = typeof seed === 'string' ? (textEncoder ||= new TextEncoder()).encode(seed) : seed;
        if (bytes.byteLength > MAX_SEED_LENGTH) {
            // TODO: Coded error.
            throw new Error(`The seed at index ${ii} exceeds the maximum length of 32 bytes`);
        }
        acc.push(...bytes);
        return acc;
    }, [] as number[]);
    const base58EncodedAddressCodec = getBase58EncodedAddressCodec();
    const programAddressBytes = base58EncodedAddressCodec.serialize(programAddress);
    const addressBytesBuffer = await crypto.subtle.digest(
        'SHA-256',
        new Uint8Array([...seedBytes, ...programAddressBytes, ...PDA_MARKER_BYTES])
    );
    const addressBytes = new Uint8Array(addressBytesBuffer);
    if (await compressedPointBytesAreOnCurve(addressBytes)) {
        // TODO: Coded error.
        throw new PointOnCurveError('Invalid seeds; point must fall off the Ed25519 curve');
    }
    return base58EncodedAddressCodec.deserialize(addressBytes)[0];
}

export async function getProgramDerivedAddress({ programAddress, seeds }: PDAInput): Promise<
    Readonly<{
        bumpSeed: number;
        pda: Base58EncodedAddress;
    }>
> {
    let bumpSeed = 255;
    while (bumpSeed > 0) {
        try {
            return {
                bumpSeed,
                pda: await createProgramDerivedAddress({
                    programAddress,
                    seeds: [...seeds, new Uint8Array([bumpSeed])],
                }),
            };
        } catch (e) {
            if (e instanceof PointOnCurveError) {
                bumpSeed--;
            } else {
                throw e;
            }
        }
    }
    // TODO: Coded error.
    throw new Error('Unable to find a viable program address bump seed');
}


