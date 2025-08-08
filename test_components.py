#!/usr/bin/env python3
"""
Simple test to verify VEXA components work
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

def test_imports():
    """Test if all imports work"""
    print("🧪 Testing VEXA imports...")
    
    try:
        from agent import VexaConfig, VexaTools
        print("✅ Agent config and tools imported successfully")
        
        from agent.core import VexaAgent
        print("✅ Agent core imported successfully")
        
        print("✅ All imports working!")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_tools():
    """Test tools without agent"""
    print("\n🛠️ Testing tools...")
    
    try:
        from agent import VexaTools
        tools = VexaTools.get_default_tools()
        print(f"✅ Got {len(tools)} tools successfully")
        
        # Test calculator
        calc_tool = VexaTools.get_calculator_tool()
        result = calc_tool.func("2+2")
        print(f"✅ Calculator test: {result}")
        
        # Test datetime
        dt_tool = VexaTools.get_datetime_tool()
        result = dt_tool.func("time")
        print(f"✅ DateTime test: {result}")
        
        return True
    except Exception as e:
        print(f"❌ Tools error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("🔍 VEXA Component Test")
    print("=" * 50)
    
    imports_ok = test_imports()
    tools_ok = test_tools()
    
    if imports_ok and tools_ok:
        print("\n🎉 All components working!")
        print("\n📋 Next steps:")
        print("   • Demo mode: python demo.py")
        print("   • Install Ollama for full functionality")
        print("   • Full agent: python app/run_agent.py (requires Ollama)")
    else:
        print("\n❌ Some components failed - check errors above")

if __name__ == "__main__":
    main()
