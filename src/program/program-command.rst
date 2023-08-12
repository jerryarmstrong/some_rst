src/program/program-command.js
==============================

Last edited: 2020-05-08 23:31:17

Contents:

.. code-block:: js

    /**
 * The commands (encoded as Transaction Instructions) that are accepted by the
 * TicTacToe Game and Dashboard program
 *
 * @flow
 */

import * as BufferLayout from 'buffer-layout';
import {PublicKey} from '@solana/web3.js';

const COMMAND_LENGTH = 8;

const Command = {
  InitDashboard: 0, // Initialize a dashboard account
  InitPlayer: 1, // Initialize a player account
  InitGame: 2, // Initialize a game account
  Advertise: 3, // Used by Player X to advertise their game
  Join: 4, // Player O wants to join
  KeepAlive: 5, // Player X/O keep alive
  Move: 6, // Player X/O mark board position (x, y)
};

function zeroPad(command: Buffer): Buffer {
  if (command.length > COMMAND_LENGTH) {
    throw new Error(
      `command buffer too large: ${command.length} > ${COMMAND_LENGTH}`,
    );
  }
  const buffer = Buffer.alloc(COMMAND_LENGTH);
  command.copy(buffer);
  return buffer;
}

function commandWithNoArgs(command: number): Buffer {
  const layout = BufferLayout.struct([BufferLayout.u32('command')]);
  const buffer = Buffer.alloc(layout.span);
  layout.encode({command}, buffer);
  return zeroPad(buffer);
}

export function initDashboard(): Buffer {
  return commandWithNoArgs(Command.InitDashboard);
}

export function initPlayer(): Buffer {
  return commandWithNoArgs(Command.InitPlayer);
}

export function initGame(): Buffer {
  return commandWithNoArgs(Command.InitGame);
}

export function advertiseGame(): Buffer {
  return commandWithNoArgs(Command.Advertise);
}

export function joinGame(): Buffer {
  return commandWithNoArgs(Command.Join);
}

export function keepAlive(): Buffer {
  return commandWithNoArgs(Command.KeepAlive);
}

export function move(x: number, y: number): Buffer {
  const layout = BufferLayout.struct([
    BufferLayout.u32('command'),
    BufferLayout.u8('x'),
    BufferLayout.u8('y'),
  ]);

  const buffer = Buffer.alloc(layout.span);
  layout.encode({command: Command.Move, x, y}, buffer);
  return zeroPad(buffer);
}

/**
 * Public key that identifies the Clock Sysvar Account Public Key
 */
export function getSysvarClockPublicKey(): PublicKey {
  return new PublicKey('SysvarC1ock11111111111111111111111111111111');
}


