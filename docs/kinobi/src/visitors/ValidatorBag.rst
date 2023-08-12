src/visitors/ValidatorBag.ts
============================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import {
  getLevelIndex,
  logDebug,
  logError,
  logInfo,
  LogLevel,
  logTrace,
  logWarn,
} from '../shared/logs';
import * as nodes from '../nodes';
import { NodeStack } from './NodeStack';

export type ValidatorItem = {
  message: string;
  level: LogLevel;
  node: nodes.Node;
  stack: NodeStack;
};

export class ValidatorBag {
  public readonly items: ValidatorItem[] = [];

  constructor(items: ValidatorItem[] = []) {
    this.items = [...items];
  }

  add(item: ValidatorItem): ValidatorBag {
    this.items.push(item);
    return this;
  }

  mergeWith(others: ValidatorBag[]): ValidatorBag {
    others.forEach((other) => {
      this.items.push(...other.items);
    });
    return this;
  }

  error(message: string, node: nodes.Node, stack: NodeStack): ValidatorBag {
    return this.add({ message, level: 'error', node, stack: stack.clone() });
  }

  warn(message: string, node: nodes.Node, stack: NodeStack): ValidatorBag {
    return this.add({ message, level: 'warn', node, stack: stack.clone() });
  }

  info(message: string, node: nodes.Node, stack: NodeStack): ValidatorBag {
    return this.add({ message, level: 'info', node, stack: stack.clone() });
  }

  trace(message: string, node: nodes.Node, stack: NodeStack): ValidatorBag {
    return this.add({ message, level: 'trace', node, stack: stack.clone() });
  }

  debug(message: string, node: nodes.Node, stack: NodeStack): ValidatorBag {
    return this.add({ message, level: 'debug', node, stack: stack.clone() });
  }

  orderByLevel(): ValidatorBag {
    const orderedItems = this.items.sort(
      (a, b) => getLevelIndex(b.level) - getLevelIndex(a.level)
    );
    return new ValidatorBag(orderedItems);
  }

  log(): void {
    this.items.forEach((item): void => {
      const hint = `Stack: ${item.stack.toString()}.`;

      switch (item.level) {
        case 'error':
          logError(item.message, hint);
          break;
        case 'warn':
          logWarn(item.message, hint);
          break;
        case 'info':
          logInfo(item.message, hint);
          break;
        case 'trace':
          logTrace(item.message, hint);
          break;
        case 'debug':
        default:
          logDebug(item.message, undefined, hint);
          break;
      }
    });
  }
}


