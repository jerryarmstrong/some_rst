apps/backend-serverless/__tests__/unit/services/step-function/start-execution-shopify-retry.service.test.ts
===========================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { StepFunctions } from 'aws-sdk';
import { startExecutionOfShopifyMutationRetry } from '../../../../src/services/step-function/start-execution-shopify-retry.service.js';

describe('unit testing start execution shopify retry', () => {
    it('should execute succesfully', async () => {
        // Set up env
        process.env.RETRY_ARN = 'some-arn';

        // Set up mock StepFunctions
        const mockStepFunctions = {
            startExecution: jest.fn().mockImplementation(() => {
                return {
                    promise: () => Promise.resolve(),
                };
            }),
        } as unknown as StepFunctions;

        // invoke startExecutionOfShopifyMutationRetry
        const mockInput = 'mock-input';
        await startExecutionOfShopifyMutationRetry(mockInput, mockStepFunctions);

        // Test
        expect(mockStepFunctions.startExecution).toHaveBeenCalledWith({
            stateMachineArn: 'some-arn',
            input: mockInput,
        });
    });
});


