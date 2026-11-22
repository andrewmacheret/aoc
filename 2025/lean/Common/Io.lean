namespace Common.Io

def readLines (path : System.FilePath) : IO (Array String) := do
  let raw <- IO.FS.readFile path
  let lines := raw.splitOn "\n"
  return lines.toArray.pop

def readInts (path : System.FilePath) : IO (Array Int) := do
  let lines <- readLines path
  return lines.map (·.toInt!)

end Common.Io
