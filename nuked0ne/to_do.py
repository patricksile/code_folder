#!/usr/bin/python3

# Todo.py
# GUI program to manage to-do tasks

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import xml.etree.ElementTree as ET
from shutil import copyfile


class Task:

    def __init__(self, index=None, subject=None, priority=None):
        self.index = index
        self.subject = subject
        self.priority = priority

class Todo(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title('Todo')
        self.master.geometry('251x306')
        self.search_var = StringVar()
        self.search_var.trace("w", self.autosearch)
        self.create_widgets()
        self.tasks = []
        self.load_tasks()

    def on_closing(self):
        self.save_all()
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()

    def create_widgets(self):
        self.search_frame = Frame(self.master)
        self.search_frame.grid(row=0, sticky=W)
        self.treeview_frame = Frame(self.master)
        self.treeview_frame.grid(row=1, sticky=W)
        self.buttons_frame = Frame(self.master)
        self.buttons_frame.grid(row=2, sticky=W)
        self.search_text = Entry(self.search_frame, width=31, textvariable=self.search_var)
        self.search_text.grid(row=0)
        self.treeview = ttk.Treeview(self.treeview_frame, height=12, columns=('Subject', 'Priority'))
        self.treeview.grid(row=0)
        self.treeview.column('#0', minwidth=0, width=35, stretch=NO, anchor=W)
        self.treeview.heading('#0', text='#')
        self.treeview.column('Subject', minwidth=0, width=156, stretch=NO, anchor=W)
        self.treeview.heading('Subject', text='Subject', command=self.sort)
        self.treeview.column('Priority', minwidth=0, width=57, stretch=NO, anchor=W)
        self.treeview.heading('Priority', text='Priority', command=self.sort)
        self.add_button = Button(self.buttons_frame, width=7, text='Add', command=self.add_item)
        self.add_button.grid(row=0, column=0)
        self.remove_button = Button(self.buttons_frame, width=7, text='Remove', command=self.remove_item)
        self.remove_button.grid(row=0, column=1)
        self.edit_button = Button(self.buttons_frame, width=7, text='Edit', command=self.edit_item)
        self.edit_button.grid(row=0, column=2)

    def create_dialog(self, item_index=None):
        self.item_dialog = Toplevel(self.master)
        self.item_dialog.geometry('202x197')
        self.item_dialog.resizable(width=False, height=False)
        self.item_dialog_text_frame = Frame(self.item_dialog)
        self.item_dialog_text_frame.grid(row=0, sticky=W)
        self.item_dialog_combobox_frame = Frame(self.item_dialog)
        self.item_dialog_combobox_frame.grid(row=1, sticky=W)
        self.item_dialog_another_frame = Frame(self.item_dialog)
        self.item_dialog_another_frame.grid(row=2)
        self.item_dialog_buttons_frame = Frame(self.item_dialog)
        self.item_dialog_buttons_frame.grid(row=3)
        self.subject_label = Label(self.item_dialog_text_frame, text='Subject:')
        self.subject_label.grid(row=0, sticky=W)
        self.subject_text = Text(self.item_dialog_text_frame, width=28, height=9)
        self.subject_text.grid(row=1)
        self.priority_label = Label(self.item_dialog_combobox_frame, text='Priority:')
        self.priority_label.grid(row=0, column=0, sticky=W)
        self.priority_combobox = ttk.Combobox(self.item_dialog_combobox_frame, width=17)
        self.priority_combobox.grid(row=0, column=1)
        self.priority_combobox['values'] = ('High', 'Medium', 'Low')
        self.item_dialog_ok_button = Button(self.item_dialog_buttons_frame, width=9, text='OK', command=self.adding_item)
        self.item_dialog_ok_button.grid(row=0, column=0)
        self.item_dialog_cancel_button = Button(self.item_dialog_buttons_frame, width=9, text='Cancel', command = self.close_dialog)
        self.item_dialog_cancel_button.grid(row=0, column=1)

        if item_index is None:
            self.item_dialog_ok_button.configure(text='Ok', command=self.adding_item)
        else:
            selected_item = self.treeview.selection()
            subject = self.treeview.item(selected_item)['values'][0]
            priority = self.treeview.item(selected_item)['values'][1]
            self.subject_text.delete('1.0', END)
            self.priority_combobox.delete(0, END)
            self.subject_text.insert(END, subject)
            self.priority_combobox.insert(0, priority)
            self.item_dialog_ok_button.configure(text='Save', command=self.save_item)

        self.item_dialog.wait_window()

    def close_dialog(self):
        self.item_dialog.destroy()

    def load_tasks(self):
        self.treeview.delete(*self.treeview.get_children())
        self.tasks.clear()
        path = os.path.expanduser('~/Documents')
        todo_path = os.path.join(path, 'Todo', 'Tasks.xml')
        if not os.path.exists(todo_path):
            if not os.path.exists(os.path.dirname(todo_path)):
                os.mkdir(os.path.dirname(todo_path))
            doc = ET.Element('Tasks')
            tree = ET.ElementTree(doc)
            tree.write(todo_path)
        else:
            tree = ET.ElementTree(file=todo_path)
        for node in tree.findall('Task'):
            t = Task(node.find('Index').text,
                     node.find('Subject').text,
                     node.find('Priority').text)
            self.tasks.append(t)
            self.treeview.insert('', END, text=t.index, values=(t.subject, t.priority))

    def save_all(self):
        path = os.path.expanduser('~/Documents')
        todo_path = os.path.join(path, 'Todo', 'Tasks.xml')
        tree = ET.ElementTree(file=todo_path)
        for xNode in tree.getroot().findall('Task'):
            tree.getroot().remove(xNode)
        for t in self.tasks:
            xTop = ET.Element('Task')
            xIndex = ET.Element('Index')
            xSubject = ET.Element('Subject')
            xPriority = ET.Element('Priority')
            xIndex.text = t.index
            xSubject.text = t.subject
            xPriority.text = t.priority
            xTop.append(xIndex)
            xTop.append(xSubject)
            xTop.append(xPriority)
            tree.getroot().append(xTop)
        tree.write(todo_path)
        self.sync()

    def add_item(self):
        self.create_dialog(item_index=None)

    def adding_item(self):
        if self.subject_text.get('1.0', '1.0 lineend') != '' and self.priority_combobox.get() != '':
            self.i = len(self.treeview.get_children())
            t = Task()
            t.index = str(self.i)
            t.subject = self.subject_text.get('1.0', '1.0 lineend')
            t.priority = self.priority_combobox.get()
            self.treeview.insert('', END, text=t.index, values=(t.subject, t.priority))
            self.i = self.i + 1
            self.tasks.append(t)
            self.close_dialog()
        else:
            messagebox.showinfo('Notification', 'Please enter subject & priority!')

    def remove_item(self):
        if len(self.treeview.selection()) > 0:
            if messagebox.askyesno('Notification', 'Are you sure you want to remove selected items?'):
                selected_items = self.treeview.selection()
                for selected_item in selected_items:
                    for i in range(len(self.tasks)):
                        if self.tasks[i].subject == self.treeview.item(selected_item)['values'][0]:
                            self.tasks.pop(i)
                            break
                    self.treeview.delete(selected_item)
        else:
            messagebox.showinfo('Notification', 'Make sure you have some items selected!')

    def edit_item(self):
        if len(self.treeview.selection()) == 1:
            if messagebox.askyesno('Notification', 'Are you sure you want to edit selected item?'):
                selected_item = self.treeview.selection()
                item_index = self.treeview.index(selected_item)
                self.create_dialog(item_index=item_index)
        else:
            messagebox.showinfo('Notification', 'Make sure you have some items selected!')

    def save_item(self):
        selected_item = self.treeview.selection()
        task = self.find_task(self.treeview.item(selected_item)['values'][0])
        task.subject = self.subject_text.get('1.0', '1.0 lineend')
        task.priority = self.priority_combobox.get()
        self.treeview.delete(selected_item)
        self.treeview.insert('', END, text=task.index, values=(task.subject, task.priority))
        self.close_dialog()

    def autosearch(self, *args):
        search_string = self.search_text.get().lower()
        self.treeview.delete(*self.treeview.get_children())
        for item in self.tasks:
            if search_string.lower() in item.subject.lower():
                self.treeview.insert('', END, text=item.index, values=(item.subject, item.priority))

    def sync(self, event=None):
        path = os.path.expanduser('~/Documents')
        todo_path = os.path.join(path, 'Todo', 'Tasks.xml')
        destination_path = os.path.expanduser('~/Dropbox/Tasks.xml')
        copyfile(todo_path, destination_path)

    def find_task(self, task):
        for x in self.tasks:
            if x.subject == task:
                return x

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def sort(self):
        columns = ('Subject', 'Priority')
        treeview = self.treeview
        for col in columns:
            treeview.heading(col, text=col, command=lambda: self.treeview_sort_column(treeview, col, False))

def main():
    root = Tk()
    gui = Todo(root)
    root.protocol('WM_DELETE_WINDOW', gui.on_closing)
    root.mainloop()

if __name__ == '__main__':
    main()
