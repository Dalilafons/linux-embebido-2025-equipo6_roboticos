from tkinter import Button, Frame, Text, END
from tkinter.ttk import Combobox, Label
from SerialDevice.serial_device import SerialDevice, BAUDRATES

class SerialDeviceBar(Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.arduino = None

        background_color = master.app_config['main_app']['background_color']
        font_family = master.config['main_app']['font_family']
        font_size = master.config['main_app']['font_size']
        font_color = master.config['main_app']['font_color']
        font_config = (font_family, font_size)

        self.serial_devices_label = Label(self, text='Pick a serial port:', font=font_config, foreground=font_color)
        self.serial_devices_combobox = Combobox(self, values=self.get_available_serial_ports(), font=font_config)
        self.baudrates_combobox = Combobox(self, values=BAUDRATES, font=font_config)

        self.send_message_label = Label(self, text='Send a message to Arduino →', font=font_config, foreground=font_color)
        self.textbox = Text(self, font=font_config, height=2, foreground=font_color)

        self.send_message_button = Button(self, text='Send Message', font=font_config, command=self.send_message)

        self.read_message_label = Label(self, text='Received a message from Arduino →', font=font_config, foreground=font_color)
        self.textbox_received_message = Text(self, font=font_config, height=2, foreground=font_color)

        self.disconnect_button = Button(self, text='Disconnect', font=font_config, command=self.disconnect_arduino)

        self.init_gui()

    def init_gui(self):
        self.serial_devices_label.pack(side='top', padx=5, pady=5, expand=True, fill='x')
        self.serial_devices_combobox.pack(side='top', padx=5, pady=5, expand=True, fill='x')
        self.baudrates_combobox.pack(side='top', padx=5, pady=5, expand=True, fill='x')

        self.serial_devices_combobox.current(0)
        self.baudrates_combobox.current(0)

        self.serial_devices_combobox.bind('<<ComboboxSelected>>', lambda event: self.connect_arduino())

        self.send_message_label.pack(side='top', padx=5, pady=5, expand=True, fill='x')
        self.textbox.pack(side='top', padx=5, pady=5, expand=True, fill='x')
        self.send_message_button.pack(side='top', padx=5, pady=5, expand=True, fill='x')
        self.read_message_label.pack(side='top', padx=5, pady=5, expand=True, fill='x')
        self.textbox_received_message.pack(side='top', padx=5, pady=5, expand=True, fill='x')
        self.disconnect_button.pack(side='top', padx=5, pady=5, expand=True, fill='x')

    def get_available_serial_ports(self):
        port_list = ['Port:']
        port_list.extend(SerialDevice.find_available_serial_ports())
        return port_list

    def connect_arduino(self):
        print("Intentando conectar con:", self.serial_devices_combobox.get(), self.baudrates_combobox.get())
        if self.arduino is None and self.serial_devices_combobox.get() != 'Port:':
            self.arduino = SerialDevice(
                port=self.serial_devices_combobox.get(),
                baudrate=int(self.baudrates_combobox.get())
            )
        elif self.serial_devices_combobox.get() != 'Port:':
            self.arduino.disconnect()
            self.arduino = SerialDevice(
                port=self.serial_devices_combobox.get(),
                baudrate=int(self.baudrates_combobox.get())
            )

    def send_message(self):
        text_to_send = self.textbox.get("1.0", END) + '\n'
        if self.arduino is not None:
            received = self.arduino.send_message(text_to_send)
            self.textbox_received_message.insert("1.0", received)
            self.textbox_received_message.insert(END, received)
    
    def disconnect_arduino(self):
        if self.arduino:
            self.arduino.disconnect()
            self.arduino = None