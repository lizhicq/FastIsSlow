@main
public struct FastIsSlow {
    public private(set) var text = "Hello, World!"

    public static func main() {
        print(FastIsSlow().text)
    }
}
