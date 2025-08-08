<template>
  <el-card shadow="hover" class="kanban-card">
    <div class="card-title">{{ card.title }}</div>
    <div v-if="card.content" class="card-content">{{ card.content }}</div>
  </el-card>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  card: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
.kanban-card {
  cursor: grab;
  background-color: #ffffff;
  border-radius: 3px;
  box-shadow: 0 1px 0 rgba(9,30,66,.25);
  margin-bottom: 8px; /* Consistent with vuedraggable gap */
}

.kanban-card:active {
    cursor: grabbing;
}

.card-title {
  font-weight: 500;
}

.card-content {
  margin-top: 8px;
  font-size: 12px;
  color: #5e6c84;
}
</style>
