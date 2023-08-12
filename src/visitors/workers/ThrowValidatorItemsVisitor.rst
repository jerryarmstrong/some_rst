src/visitors/workers/ThrowValidatorItemsVisitor.ts
==================================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    /* eslint-disable no-console */
import chalk from 'chalk';
import { getLevelIndex, LogLevel } from '../../shared/logs';
import { BaseDelegateVisitor } from '../BaseDelegateVisitor';
import { ValidatorBag } from '../ValidatorBag';
import { Visitor } from '../Visitor';

export class ThrowValidatorItemsVisitor extends BaseDelegateVisitor<
  ValidatorBag,
  void
> {
  constructor(
    validator: Visitor<ValidatorBag>,
    readonly throwLevel: LogLevel = 'error'
  ) {
    super(validator);
  }

  map(validatorBag: ValidatorBag): void {
    const bag = validatorBag.orderByLevel();
    bag.log();

    const levelHistogram = bag.items.reduce((acc, item) => {
      acc[item.level] = (acc[item.level] ?? 0) + 1;
      return acc;
    }, {} as Record<LogLevel, number>);
    const maxLevel = Object.keys(levelHistogram)
      .map((level) => getLevelIndex(level as LogLevel))
      .sort((a, b) => b - a)[0];

    if (maxLevel >= getLevelIndex(this.throwLevel)) {
      const histogramString = Object.keys(levelHistogram)
        .map((level) => `${level}s: ${levelHistogram[level as LogLevel]}`)
        .join(', ');
      console.log(
        `${chalk.red(`Failed to validate the nodes.`)} ` +
          `${chalk.red.bold(`Found ${histogramString}.`)}\n`
      );
      process.exit(1);
    }
  }
}


