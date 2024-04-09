import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;

public class SimpleBrowser extends JFrame {
    public SimpleBrowser() {
        super("Simple Browser");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTextField urlField = new JTextField("http://", 30);
        JButton goButton = new JButton("Go");
        JEditorPane displayPane = new JEditorPane();
        displayPane.setEditable(false);
        displayPane.setContentType("text/html");

        goButton.addActionListener(e -> loadURL(urlField.getText(), displayPane));
        urlField.addActionListener(e -> loadURL(urlField.getText(), displayPane));

        JPanel topPanel = new JPanel();
        topPanel.add(new JLabel("URL:"));
        topPanel.add(urlField);
        topPanel.add(goButton);

        getContentPane().add(topPanel, BorderLayout.NORTH);
        getContentPane().add(new JScrollPane(displayPane), BorderLayout.CENTER);

        setSize(800, 600);
        setLocationRelativeTo(null); // Centraliza a janela
        setVisible(true);
    }

    private void loadURL(String urlString, JEditorPane displayPane) {
        try {
            URI uri = new URI(urlString);
            Desktop.getDesktop().browse(uri);
        } catch (URISyntaxException | IOException e) {
            JOptionPane.showMessageDialog(this, "Erro ao carregar URL: " + e.getMessage(),
                    "Erro", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SimpleBrowser::new);
    }
}
