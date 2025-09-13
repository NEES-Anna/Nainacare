import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

// Tumhara live API URL
const apiBase = "https://nainacare-api-271195772091.asia-south1.run.app";

void main() {
  runApp(const NainaCareApp());
}

class NainaCareApp extends StatelessWidget {
  const NainaCareApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "NainaCare Lite",
      theme: ThemeData(primarySwatch: Colors.pink),
      home: const MoodPage(),
    );
  }
}

class MoodPage extends StatefulWidget {
  const MoodPage({super.key});

  @override
  State<MoodPage> createState() => _MoodPageState();
}

class _MoodPageState extends State<MoodPage> {
  final TextEditingController c = TextEditingController();
  String? summary;

  Future<void> sendMood() async {
    final r = await http.post(
      Uri.parse("$apiBase/api/summary"),
      headers: {
        "Authorization": "Bearer test",
        "Content-Type": "application/json",
      },
      body: json.encode({"text": c.text}),
    );

    if (r.statusCode == 200) {
      final data = json.decode(r.body);
      setState(() => summary = data["summary"]);
    } else {
      setState(() => summary = "Error: ${r.statusCode}");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("💖 NainaCare Lite")),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: c,
              decoration: const InputDecoration(
                labelText: "How are you feeling today?",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: sendMood,
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 15),
              ),
              child: const Text("Save & Analyze"),
            ),
            const SizedBox(height: 30),
            if (summary != null)
              Card(
                color: Colors.pink[50],
                margin: const EdgeInsets.all(10),
                child: Padding(
                  padding: const EdgeInsets.all(15),
                  child: Text(summary!, style: const TextStyle(fontSize: 18)),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
