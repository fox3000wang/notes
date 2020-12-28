// Vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
  },
});

// 你看到的 v-bind attribute 被称为指令。
// 指令带有前缀 v-，以表示它们是 Vue 提供的特殊 attribute。
// 可能你已经猜到了，它们会在渲染的 DOM 上应用特殊的响应式行为。
// 在这里，该指令的意思是：“将这个元素节点的 title attribute 和 Vue 实例的 message property 保持一致”。
var app2 = new Vue({
  el: '#app-2',
  data: {
    message: '页面加载于 ' + new Date().toLocaleString(),
  },
});

// 继续在控制台输入 app3.seen = false，你会发现之前显示的消息消失了
var app3 = new Vue({
  el: '#app-3',
  data: {
    seen: true,
  },
});

// 在控制台里，输入 app4.todos.push({ text: '新项目' })，你会发现列表最后添加了一个新项目。
var app4 = new Vue({
  el: '#app-4',
  data: {
    todos: [
      { text: '学习 JavaScript' },
      { text: '学习 Vue' },
      { text: '整个牛项目' },
    ],
  },
});

// 注意在 reverseMessage 方法中，我们更新了应用的状态，但没有触碰 DOM——所有的 DOM 操作都由 Vue 来处理，你编写的代码只需要关注逻辑层面即可。
var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'Hello Vue.js!',
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('');
    },
  },
});

// Vue 还提供了 v-model 指令，它能轻松实现表单输入和应用状态之间的双向绑定。
var app6 = new Vue({
  el: '#app-6',
  data: {
    message: 'Hello Vue!',
  },
});

// 定义名为 todo-item 的新组件
Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>',
});

var app7 = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      { id: 0, text: '蔬菜' },
      { id: 1, text: '奶酪' },
      { id: 2, text: '随便其它什么人吃的东西' },
    ],
  },
});
