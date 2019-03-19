import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure

class MyWindow(Gtk.Window):

    def __init__(self):  # c-tor
        Gtk.Window.__init__(self, title="Project IOM")
        self.set_border_width(15)  # add space between between content and edges
        self.set_default_size(800, 600)

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Calcul TF Proiect IOM"
        self.set_titlebar(header_bar)

        #Fency button on right
        audio_button = Gtk.Button()
        msr = Gio.ThemedIcon(name = "mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(msr, Gtk.IconSize.BUTTON)
        audio_button.add(image)
        header_bar.pack_end(audio_button) # pack end ca sa apara in dreapta

        # Create box of linked items
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")  # whatever we put, there will be a linked

        # Left arrow
        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(left_arrow)
        left_arrow.connect("clicked", self.left)

        # Right arrow
        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(right_arrow)
        left_arrow.connect("clicked", self.right)

        # Tre sa includem box-ul in header
        header_bar.pack_start(box)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.grid = Gtk.Grid(column_homogeneous=False,
                         column_spacing=10,
                         row_spacing=30)
        self.add(self.grid)
        self.notebook.append_page(self.grid, Gtk.Label('Ipoteza'))
        self.grid.set_border_width(10)

        label1 = Gtk.Label()
        label1.set_markup("<big>Generati un semnal sinusoidal cu: </big>")
        label1.set_line_wrap(True)

        label2 = Gtk.Label()
        label2.set_markup("<big>frecventa: </big>")

        label3 = Gtk.Label()
        label3.set_markup("<big>durata: </big>")

        label4 = Gtk.Label()
        label4.set_markup("<big>frecventa de estantionare: </big>")

        self.label51 = Gtk.Label()
        #self.label5.set_markup("<big> </big>")
        self.label52 = Gtk.Label()
        self.label53 = Gtk.Label()

        label6 = Gtk.Label()
        label6.set_markup("<big> Hz </big>")

        label7 = Gtk.Label()
        label7.set_markup("<big> s </big>")

        label8 = Gtk.Label()
        label8.set_markup("<big> Hz </big>")


        adjustment = Gtk.Adjustment(5, 0, 100, 1, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)

        check_numeric1 = Gtk.CheckButton("Numeric")
        check_numeric1.connect("toggled", self.on_numeric_toggled)

        check_numeric2 = Gtk.CheckButton("Numeric")
        check_numeric2.connect("toggled", self.on_numeric_toggled)

        check_numeric3 = Gtk.CheckButton("Numeric")
        check_numeric3.connect("toggled", self.on_numeric_toggled)

        check_ifvalid1 = Gtk.CheckButton("If Valid")
        check_ifvalid1.connect("toggled", self.on_ifvalid_toggled)

        check_ifvalid2 = Gtk.CheckButton("If Valid")
        check_ifvalid2.connect("toggled", self.on_ifvalid_toggled)

        check_ifvalid3 = Gtk.CheckButton("If Valid")
        check_ifvalid3.connect("toggled", self.on_ifvalid_toggled)

        adjustment2 = Gtk.Adjustment(1, 0, 100, 1, 10, 0)
        self.spinbutton2 = Gtk.SpinButton()
        self.spinbutton2.set_adjustment(adjustment2)

        adjustment3 = Gtk.Adjustment(150, 0, 1000, 1, 10, 0)
        self.spinbutton3 = Gtk.SpinButton()
        self.spinbutton3.set_adjustment(adjustment3)

        button10 = Gtk.Button("Salvati fq")
        button10.connect("clicked", self.button_pressed1)

        button11 = Gtk.Button("Salvati durata")
        button11.connect("clicked", self.button_pressed2)

        button12 = Gtk.Button("Salvati fq es")
        button12.connect("clicked", self.button_pressed3)

        button_about = Gtk.Button("About")
        button_about.connect("clicked", self.button_about)



        self.grid.attach(label1, 0, 1, 1, 1)
        self.grid.attach(label2, 0, 3, 1, 1)
        self.grid.attach(label3, 0, 5, 1, 1)
        self.grid.attach(label4, 0, 7, 1, 1)
        self.grid.attach(self.spinbutton, 1, 3, 1, 1)
        self.grid.attach(self.spinbutton2, 1, 5, 1, 1)
        self.grid.attach(self.spinbutton3, 1, 7, 1, 1)
        self.grid.attach(check_numeric1, 3, 3, 1, 1)
        self.grid.attach(check_numeric2, 3, 5, 1, 1)
        self.grid.attach(check_numeric3, 3, 7, 1, 1)
        self.grid.attach(check_ifvalid1, 4, 3, 1, 1)
        self.grid.attach(check_ifvalid2, 4, 5, 1, 1)
        self.grid.attach(check_ifvalid3, 4, 7, 1, 1)
        self.grid.attach(label6, 2, 3, 1, 1)
        self.grid.attach(label7, 2, 5, 1, 1)
        self.grid.attach(label8, 2, 7, 1, 1)
        self.grid.attach(button10, 1, 9, 1, 1)
        self.grid.attach(button11, 1, 10, 1, 1)
        self.grid.attach(button12, 1, 11, 1, 1)
        self.grid.attach(self.label51, 2, 9, 1, 1)
        self.grid.attach(self.label52, 2, 10, 1, 1)
        self.grid.attach(self.label53, 2, 11, 1, 1)
        self.grid.attach(button_about, 1, 12, 1, 1)

        self.page2 = Gtk.Grid(column_homogeneous=False,
                         column_spacing=10,
                         row_spacing=30)
        self.page2.set_border_width(10)
        self.notebook.append_page(self.page2, Gtk.Label("Calc TFF"))

        label10 = Gtk.Label()
        label10.set_markup("<big>Calculati transformata Fourier\nrapida a semnalului generat, in: </big>")
        label10.set_line_wrap(True)

        adjustment4 = Gtk.Adjustment(1024, 0, 100000, 1, 10, 0)
        self.spinbutton4 = Gtk.SpinButton()
        self.spinbutton4.set_adjustment(adjustment4)

        label11 = Gtk.Label()
        label11.set_markup("<big> puncte </big>")

        check_numeric4 = Gtk.CheckButton("Numeric")
        check_numeric4.connect("toggled", self.on_numeric_toggled)

        button2 = Gtk.Button("Calc TFF")
        button2.connect("clicked", self.tff)

        self.label12 = Gtk.Label("")

        button_about2 = Gtk.Button("About")
        button_about2.connect("clicked", self.button_about)

        check_ifvalid21 = Gtk.CheckButton("If Valid")
        check_ifvalid21.connect("toggled", self.on_ifvalid_toggled)

        button21 = Gtk.Button("Salvati nr puncte")
        button21.connect("clicked", self.button_pressed21)

        self.label21 = Gtk.Label("")



        self.page2.attach(label10, 0, 0, 1, 1)
        self.page2.attach(self.spinbutton4, 0, 2, 1, 1)
        self.page2.attach(label11, 1, 2, 1, 1)
        self.page2.attach(button2, 0, 5, 1, 1)
        self.page2.attach(self.label12, 0, 6, 1, 1)
        self.page2.attach(check_numeric4, 2, 2, 1, 1)
        self.page2.attach(check_ifvalid21, 3, 2, 1, 1)
        self.page2.attach(button21, 0, 3, 1, 1)
        self.page2.attach(self.label21, 1, 3, 1, 1)
        self.page2.attach(button_about2, 1, 7, 1, 1)

        self.page3 = Gtk.Grid(column_homogeneous=False,
                         column_spacing=10,
                         row_spacing=30)
        self.page3.set_border_width(10)
        self.notebook.append_page(self.page3, Gtk.Label("Reprezentari Grafice"))

        label13 = Gtk.Label()
        label13.set_markup("<big>Afisati semnalul generat si spectrul de putere al acestuia:</big>")

        button3 = Gtk.Button("Afisati semnalul generat")
        button3.connect("clicked", self.asg)

        button4 = Gtk.Button("Afisati spectru de putere")
        button4.connect("clicked", self.asp)

        button_about3 = Gtk.Button("About")
        button_about3.connect("clicked", self.button_about)

        self.page3.attach(label13, 0, 0, 1, 1)
        self.page3.attach(button3, 0, 1, 2, 2)
        self.page3.attach(button4, 0, 2, 2, 2)
        self.page3.attach(button_about3, 1, 4, 2, 2)


        self.page4 = Gtk.ScrolledWindow()
        self.notebook.append_page(self.page4, Gtk.Label("S sin generat"))
        self.page4.set_border_width(10)

        self.page5 = Gtk.ScrolledWindow()
        self.notebook.append_page(self.page5, Gtk.Label("Spectrul de putere"))
        self.page5.set_border_width(10)

        self.page6 = Gtk.Grid(column_homogeneous=False,
                         column_spacing=10,
                         row_spacing=30)
        self.notebook.append_page(self.page6, Gtk.Label("Calc Perioada"))
        self.page6.set_border_width(10)

        label14 = Gtk.Label()
        label14.set_markup("<big>Pe baza spectrului de putere, calculati perioada semnalului</big>")

        button5 = Gtk.Button("Calc perioada")
        button5.connect("clicked", self.cp)


        self.label15= Gtk.Label("Rezultat")


        image2 = Gtk.Button()
        image = Gtk.Image.new_from_file("eminem.jpg")
        image2.add(image)


        self.page6.attach(label14, 0, 0, 1, 1)
        self.page6.attach(button5, 0, 1, 1, 1)
        self.page6.attach(self.label15, 0, 2, 1, 1)
        self.page6.attach(image2, 0, 3, 1, 1)


    def button_pressed1(self, widget):
        port = self.spinbutton.get_value()
        a = str(int(port))
        self.label51.set_text(a)


    def button_pressed2(self, widget):
        port = self.spinbutton2.get_value()
        a = str(int(port))
        self.label52.set_text(a)


    def button_pressed3(self, widget):
        port = self.spinbutton3.get_value()
        a = str(int(port))
        self.label53.set_text(a)


    def button_pressed21(self, widget):
        port = self.spinbutton4.get_value()
        a = str(int(port))
        self.label21.set_text(a)


    def tff(self, widget):
        f = self.spinbutton.get_value()
        fs = self.spinbutton3.get_value()
        tfinal = self.spinbutton2.get_value()
        t = np.arange(0, tfinal, 1./fs)

        x = np.sin(2 * 3,14 * f * t)

        nfft = self.spinbutton4.get_value()
        X = np.fft.fft(x, int(nfft))
        Xabs = np.abs(X)
        xHz = (np.arange(0, nfft/2.) * fs) / nfft
        self.label12.set_text(str(X))

    def button_about(self, widget):
        dialog = PopUp(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("You clicked the ok button")
        elif response == Gtk.ResponseType.CANCEL:
            print("You clicked the CANCEL button")

        dialog.destroy()


    def asg(self, widget):
        f1 = Figure(figsize=(5, 4), dpi=100)
        a1 = f1.add_subplot(111)
        f = self.spinbutton.get_value()
        fs = self.spinbutton3.get_value()
        s2 = self.spinbutton2.get_value()

        t1 = np.arange(0, s2, 1./fs)
        x = np.sin(2 * np.pi * f* t1)
        a1.plot(t1, x)

        canvas = FigureCanvas(f1)  # Gtk.DrawingArea
        canvas.set_size_request(600, 400)
        canvas.show()
        self.page4.add_with_viewport(canvas)


    def asp(self, widget):
        f2 = Figure(figsize=(5, 4), dpi=100)
        a2 = f2.add_subplot(111)
        f = self.spinbutton.get_value()
        fs = self.spinbutton3.get_value()
        s2 = self.spinbutton2.get_value()

        t1 = np.arange(0, s2, 1. / fs)
        x = np.sin(2 * np.pi * f * t1)
        nfft = self.spinbutton4.get_value()
        X = np.fft.fft(x, int(nfft))
        Xabs = np.abs(X)
        xHz = (np.arange(0, nfft / 2.) * fs) / nfft

        a2.plot(xHz, Xabs[:int(nfft/2)])

        canvas = FigureCanvas(f2)  # Gtk.DrawingArea
        canvas.set_size_request(600, 400)
        canvas.show()
        self.page5.add_with_viewport(canvas)


    def cp(self, widget):
        f = int(self.spinbutton.get_value())
        fs = int(self.spinbutton3.get_value())
        tfinal = int(self.spinbutton2.get_value())
        t = np.arange(0, tfinal, 1./fs)

        x = np.sin(2 * np.pi * f * t)

        nfft = int(self.spinbutton4.get_value())
        X = np.fft.fft(x, int(nfft))
        Xabs = np.abs(X)
        xHz = (np.arange(0, nfft/2.) * fs) / nfft
        idx = np.argmax(Xabs[:int(nfft / 2)])
        per = 1 / xHz[idx]
        self.label15.set_text(str(per))


    def on_numeric_toggled(self, button):
        self.spinbutton.set_numeric(button.get_active())


    def on_ifvalid_toggled(self, button):
        if button.get_active():
            policy = Gtk.SpinButtonUpdatePolicy.IF_VALID
        else:
            policy = Gtk.SpinButtonUpdatePolicy.ALWAYS
        self.spinbutton.set_update_policy(policy)


    def left(self, widget):
        self.notebook.set_current_page(0)
        self.notebook.prev_page()


    def right(self, widget):
        self.notebook.set_current_page(0)
        self.notebook.next_page()


class PopUp(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "About", parent, Gtk.DialogFlags.MODAL, (
            "Cancel", Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        ))
        # MODAL-> obliga user ul sa se ocupe de pop up mai intai
        self.set_default_size(200, 100)
        self.set_border_width(30)

        label = Gtk.Label()
        label.set_markup("GUI APP made \nusing PyGobject\n\nVersion 1.1\n"
                         "<a href=\"https://python-gtk-3-tutorial.readthedocs.io/en/latest/\" title = \"Hover text\">Official Site</a>\n"
                         "<small>(c) DC9697</small>\n")

        box = self.get_content_area()
        box.add(label)
        self.show_all()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()