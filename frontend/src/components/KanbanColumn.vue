<template>
  <el-card class="column-card">
    <template #header>
      <div class="column-header">
        <span>{{ column.title }}</span>
      </div>
    </template>
    <draggable
      v-model="column.cards"
      group="cards"
      item-key="id"
      class="card-draggable"
      ghost-class="ghost"
      @end="onCardDragEnd"
    >
      <template #item="{ element: card }">
        <KanbanCard :card="card" />
      </template>
    </draggable>
  </el-card>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
import draggable from 'vuedraggable';
import KanbanCard from './KanbanCard.vue';

const props = defineProps({
  column: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['update-board']);

const onCardDragEnd = () => {
  // When a card is moved, notify the parent board to persist the changes
  emit('update-board');
};
</script>

<style scoped>
.column-card {
  background-color: #ebecf0;
}
.column-header {
  font-weight: bold;
  color: #172b4d;
}
.card-draggable {
  min-height: 100px; /* Provides a drop zone even when empty */
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}
</style>
