import React from 'react';
import { Alert, Box, Button, Card, Group, Text, TextInput } from '@mantine/core';
import { useForm } from '@mantine/form';
import axios from 'axios';

export const WordCounter = () => {
  const [wordsCounter, setWordsCounter] = React.useState(0);
  const [error, setError] = React.useState(null);

  const form = useForm({
    initialValues: { text: '' },
    validate: {
      text: (value) => {
        if (value.length < 1) {
          return 'Please enter a text';
        }
      }
    }
  });

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost/api/v1/words-counter', {
        words_string: form.values.text
      });

      setWordsCounter(response.data.words_count);
    } catch (error) {
      setError(`Error: ${error}`);
    }
  };

  return (
    <Box
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh'
      }}>
      <Card
        shadow="md"
        p="lg"
        radius="md"
        withBorder
        style={{ backgroundColor: '#e1ebee', height: '17vh', width: '50vh' }}>
        <Text style={{ fontSize: '50px', textAlign: 'center' }}>Words Counter</Text>

        <form
          onSubmit={form.onSubmit((values) => {
            form.setValues(values);
            handleSubmit();
          })}>
          <TextInput
            placeholder="Start typing..."
            value={form.values.text}
            // style={{ height: '50%' }}
            {...form.getInputProps('text')}
          />
          {error && (
            <Alert mt="xs" color="red">
              {error}
            </Alert>
          )}

          <Text mt="xs">Words count: {wordsCounter}</Text>

          <Group style={{ justifyContent: 'end', display: 'flex' }} mt="md">
            <Button
              onClick={() => {
                form.reset();
                setWordsCounter(0);
              }}
              color="red">
              Reset
            </Button>
            <Button type="submit">Count words</Button>
          </Group>
        </form>
      </Card>
    </Box>
  );
};
