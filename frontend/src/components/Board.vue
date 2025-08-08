<template>
  <div class="board-container">
    <draggable
      v-model="board.columns"
      group="columns"
      item-key="id"
      class="board-draggable"
      @end="onColumnDragEnd"
    >
      <template #item="{ element: column }">
        <div class="column-wrapper">
          <KanbanColumn :column="column" @update-board="updateBoard" />
        </div>
      </template>
    </draggable>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import draggable from 'vuedraggable';
import KanbanColumn from './KanbanColumn.vue';

const board = ref({ columns: [] });

const API_URL = 'http://localhost:8000/api/board';

const fetchBoard = async () => {
  try {
    const response = await axios.get(API_URL);
    board.value = response.data;
  } catch (error) {
    console.error('Error fetching board data:', error);
  }
};

const updateBoard = async () => {
  try {
    await axios.put(API_URL, board.value);
  } catch (error) {
    console.error('Error updating board:', error);
    // Optionally, revert local changes or show an error message
  }
};

const onColumnDragEnd = () => {
  // When a column is moved, persist the new order
  updateBoard();
};

onMounted(() => {
  fetchBoard();
});
</script>

<style scoped>
.board-container {
  padding: 20px;
  background-color: #f0f2f5;
  min-height: 100vh;
}
.board-draggable {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}
.column-wrapper {
  min-width: 300px;
  max-width: 300px;
}
</style>
