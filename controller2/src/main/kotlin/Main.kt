package wholenote.controller

import edu.cmu.sphinx.api.Configuration
import edu.cmu.sphinx.api.LiveSpeechRecognizer

fun main() {
    println("Hello Kotlin/Native!")

    val configuration = Configuration()

    configuration.acousticModelPath = "resource:/models/en-us/en-us"
    configuration.dictionaryPath = "resource:/models/en-us/cmudict-en-us.dict"
    configuration.languageModelPath = "resource:/models/en-us/en-us.lm.bin"

    val recognizer = LiveSpeechRecognizer(configuration)
    recognizer.startRecognition(true)

    var result = recognizer.result
    while (result != null) {
        System.out.format("Hypothesis: %s\n", result.hypothesis)
        result = recognizer.result
    }
    recognizer.stopRecognition()
}
